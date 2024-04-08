from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def query_chatgpt(client, prompt_base, model, role, pdf_text):
    print(f"Querying with {model} model...")
    messages = [
        {"role": "system", "content": role},
        {"role": "user", "content": prompt_base + "\n" + pdf_text}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=4096
    )
    print("Response received!")
    return response.choices[0].message.content


def send_chunks_to_api(chunks, model="text-davinci-003", prompt_base="",
                       role="You are a specialist in data extraction. Extract product information from the text.",
                       client=None):
    """
    Envoie parallèlement les blocs de texte à l'API ChatGPT et garde trace des échecs.

    Args:
        chunks (list of str): Blocs de texte extraits du PDF.
        model (str): Modèle ChatGPT à utiliser. Exemple : "text-davinci-003"
        prompt_base (str): Base du prompt à envoyer à l'API.
        role (str): Rôle défini pour le modèle.
        client (openai.OpenAI): Client OpenAI initialisé.

    Returns:
        tuple:
            list of str: Réponses réussies de l'API pour chaque bloc.
            list of str: Textes des requêtes échouées.
    """
    successful_responses = []
    failed_requests = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_chunk = {executor.submit(query_chatgpt, client, prompt_base, model, role, chunk): chunk for chunk in
                           chunks}

        for future in as_completed(future_to_chunk):
            chunk = future_to_chunk[future]
            try:
                response = future.result()
                successful_responses.append(response)
            except Exception as exc:
                print(f'Requête pour le chunk échouée: {exc}')
                failed_requests.append(chunk)  # Ajoute le chunk échoué à la liste des échecs

    return successful_responses, failed_requests
