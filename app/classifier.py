from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = ["Produtivo", "Improdutivo"]

def classify_email(text: str):
    result = classifier(text, LABELS)
    label = result["labels"][0]
    confidence = round(result["scores"][0], 2)

    if label == "Produtivo":
        response = (
            "Olá! Recebemos sua solicitação e ela está em análise. "
            "Em breve retornaremos com mais informações."
        )
    else:
        response = "Obrigado pela mensagem! Desejamos um excelente dia 😊"

    return {
        "classification": label.upper(),
        "response": response,
        "confidence": confidence
    }
