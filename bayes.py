# iMPORTAR AS BIBLIOTECAS
import streamlit as st
import fitz

# função para extrair os arquivos     
def extract_files(uploader):
    text = ""
    for pdf in uploader:
        with fitz.open(stream=pdf.read(), filetype="pdf") as doc: 
            for page in doc:
                text += page.get_text("text") 
    return text

def chat_with_groq(prompt, context):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        message = [
            {"role": "system", "content": "Voce e um assistente que reponde os dados do pdf e ajuda na minha rotina de estudos"},
            {"role": "user", "content": f"{context}\n\nPergunta: {prompt}}
        ]
    )
    return response.choice[0].message.content
    
# CRIAR A INTERFACE
def main():
    st.title("Bagulho de organização de estudos")
    # Incluir uma imagem de acordo ao sistema escolhido
    with st.sidebar:
        st.header("UPLoader Files")
        uploader = st.file_uploader("Adicione arquivos", type="pdf", accept_multiple_files=True)
    if uploader:
        text = extract_files(uploader)
        st.session_state["document-text"] = text
    user_input = st.text_input("Digite a sua pergunta")
    chat_with_groq(user_input, text)

if __name__ == "__main__":
    main()
