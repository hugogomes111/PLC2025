# Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:



# EXERCICIO 1

'''
Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`
Out: `<h1>Exemplo</h1>`



Bold: pedaços de texto entre "**":

In: `Este é um **exemplo** ...`
Out: `Este é um <b>exemplo</b> ...`



Itálico: pedaços de texto entre "*":

In: `Este é um *exemplo* ...`
Out: `Este é um <i>exemplo</i> ...`



Lista numerada:

In:
1. Primeiro item
2. Segundo item
3. Terceiro item
Out:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>


Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`
Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`



Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`
Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

'''


def markdown_to_html(markdown_text):
    html_text = markdown_text
    # Cabeçalhos
    html_text = html_text.replace('### ', '<h3>').replace('\n', '</h3>\n', 1)
    html_text = html_text.replace('## ', '<h2>').replace('\n', '</h2>\n', 1)
    html_text = html_text.replace('# ', '<h1>').replace('\n', '</h1>\n', 1)
    # Bold
    html_text = html_text.replace('**', '<b>').replace('<b>', '</b>', 1)
    # Itálico
    html_text = html_text.replace('*', '<i>').replace('<i>', '</i>', 1)
    # Lista numerada
    if '1. ' in html_text:
        html_text = html_text.replace('1. ', '<ol>\n<li>').replace('\n2. ', '</li>\n<li>').replace('\n3. ', '</li>\n<li>').replace('\n', '</li>\n', 1) + '</li>\n</ol>'
    # Link
    while '[' in html_text and ']' in html_text and '(' in html_text and ')' in html_text:
        start_text = html_text.index('[')
        end_text = html_text.index(']')
        start_url = html_text.index('(', end_text)
        end_url = html_text.index(')', start_url)
        link_text = html_text[start_text + 1:end_text]
        link_url = html_text[start_url + 1:end_url]
        html_link = f'<a href="{link_url}">{link_text}</a>'
        html_text = html_text[:start_text] + html_link + html_text[end_url + 1:]
    # Imagem
    while '!' in html_text and '[' in html_text and ']' in html_text and '(' in html_text and ')' in html_text:
        start_alt = html_text.index('![')
        end_alt = html_text.index(']')
        start_src = html_text.index('(', end_alt)
        end_src = html_text.index(')', start_src)
        alt_text = html_text[start_alt + 2:end_alt]
        img_src = html_text[start_src + 1:end_src]
        html_img = f'<img src="{img_src}" alt="{alt_text}"/>'
        html_text = html_text[:start_alt] + html_img + html_text[end_src + 1:]
    return html_text        

# Exemplo de uso
markdown_example = '''# Exemplo de Cabeçalho 1          
## Exemplo de Cabeçalho 2
### Exemplo de Cabeçalho 3  
Este é um **exemplo** de texto em negrito e este é um *exemplo* de texto em itálico.
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...'''

html_output = markdown_to_html(markdown_example)
print(html_output)


