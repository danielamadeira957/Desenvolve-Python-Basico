import emoji 
#lista de emoji
print("emojis disponíveis:")
print(":star_struck:")
print(":smiling_with_tear:")
print(":face_with_rolling_eyes:")
print(":ziper_mouth_face:")

#solicitar a frase ao usuário
frase = input ("\nDigite uma frase e ela será emojizada: ")
#utilizar a função emojize para converter o texto
#o parâmetro language='alias' ajuda a reconhecer códigos comuns
frase_emojizada = emoji.emojize ( frase, language='alias')

#apresentar o resultado
print (f"Frase emojizada: {frase_emojizada}")