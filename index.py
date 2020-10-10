from browser import document, alert, bind, console
from datetime import date
import random

@bind(document.select('.checkbox'), 'change')
def handlerCheckbox(event):
    if event.target.checked:
        document.select('.type p')[0].innerHTML = 'Descriptografar'
        document['input-submit'].value = 'Descriptografar'
        document.select('.type p')[0].style.backgroundColor = '#AB3A40'
    else:
        document.select('.type p')[0].innerHTML = 'Criptografar'
        document['input-submit'].value = 'Criptografar'
        document.select('.type p')[0].style.backgroundColor = '#222'

# SUBMIT DO FORMULARIO
@bind(document['crypt-decimal-form'], 'submit')
def handlerSubmit(event):

    # CAIXA DE MENSAGEM
    def showCustomMessage(pTitle, pBody):
        document['crypt-message-title'].innerHTML = pTitle
        document['crypt-message-body'].innerHTML = document['crypt-message-body'].innerHTML + "<br>" + pBody
        document['crypt-message'].style.display = 'inline'

    inputValue = document['input-crypt'].value
    selectValue = document['chars-select'].options

    # Input não está vazio && criptografar ou descriptografar
    if inputValue and not document.select('.checkbox')[0].checked:
        auxToNumber = []
        auxToChar = ''

        # Buscando valor selecionado no SELECT
        for options in selectValue:
            if options.selected:
                selectValue = options.value
        
        # Valor aleatório no SELECT
        if selectValue == '*':
            selectValue = random.randint(97, 122)
        else:
            selectValue = ord(selectValue.lower())

        # For tamanho da entrada
        for char in range(len(inputValue)):
            # Chave no fim do alfabeto
            if (ord(inputValue[char].lower()) + (selectValue - 97)) > 122:
                auxToNumber.append(ord(inputValue[char].lower()) + ((selectValue - 97) - 26))
            else:   
                auxToNumber.append(ord(inputValue[char].lower()) + (selectValue - 97))

            # Se original está em maiusculo
            if inputValue[char].isupper():
                auxToChar = auxToChar + chr(auxToNumber[char]).upper()
            else:
                auxToChar = auxToChar + chr(auxToNumber[char])

        # Deu certo
        showCustomMessage('"'+inputValue+'"' + ' pela chave ' + '"'+chr(selectValue)+'"' + ' para:', auxToChar)
    elif inputValue and document.select('.checkbox')[0].checked:
        auxToNumber = []
        auxToChar = ''

        # Buscando valor selecionado no SELECT
        for options in selectValue:
            if options.selected:
                selectValue = options.value

        if selectValue == '*':
            for letter in range(26):
                auxToNumber = []
                auxToChar = ''

                for char in range(len(inputValue)):
                    if (ord(inputValue[char].lower()) + letter) > 122:
                        auxToNumber.append((97 + ((ord(inputValue[char].lower()) + letter) - 123)))
                    else:
                        auxToNumber.append((ord(inputValue[char].lower()) + letter))

                    # ESPAÇO
                    if not (auxToNumber[char] >= 97 and auxToNumber[char] <= 122):
                        auxToNumber[char] = 32

                    # Se original está em maiusculo
                    if inputValue[char].isupper():
                        auxToChar = auxToChar + chr(auxToNumber[char]).upper()
                    else:
                        auxToChar = auxToChar + chr(auxToNumber[char])

                # Deu certo
                showCustomMessage('"'+inputValue+'"' + ' pela chave ' + '"'+"*"+'"' + ' para:', auxToChar)
        else:
            selectValue = ord(selectValue.lower())

            for char in range(len(inputValue)):
                if ((ord(inputValue[char].lower()) - 97) - (selectValue - 97)) >= 0:
                    auxToNumber.append((97 + ((ord(inputValue[char].lower()) - 97) - (selectValue - 97))))
                else:
                    auxToNumber.append((123 + ((ord(inputValue[char].lower()) - 97) - (selectValue - 97))))
                    
                # ESPAÇO
                if not (auxToNumber[char] >= 97 and auxToNumber[char] <= 122):
                    auxToNumber[char] = 32

                # Se original está em maiusculo
                if inputValue[char].isupper():
                    auxToChar = auxToChar + chr(auxToNumber[char]).upper()
                else:
                    auxToChar = auxToChar + chr(auxToNumber[char])
            # Deu certo
            showCustomMessage('"'+inputValue+'"' + ' pela chave ' + '"'+chr(selectValue)+'"' + ' para:', auxToChar)
    else:
        # Ocorreu um erro
        showCustomMessage('Acho que o campo está vazio', 'Não há o que criptografar... Escreve alguma coisa e tenta de novo!')

    document['input-crypt'].value = ''
    document['input-crypt'].focus()
    event.preventDefault()


document['swag_creator'].innerHTML = 'GMUtils &copy; {}'.format(date.today().year)
