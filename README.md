
# Automação de consulta de email

<p>Este é um projeto em Python que usa a biblioteca <code>imaplib</code> para consultar uma conta de email e notificar sobre novas mensagens por meio da biblioteca <code>win10toast</code>. O código faz uma busca por emails recebidos em um ano específico e filtra as mensagens por palavras-chave no assunto.</p>

<p>Ao encontrar uma nova mensagem que contém uma das palavras-chave, o código imprime informações relevantes na tela e envia uma notificação para o desktop.</p>

## Configuração
<p>Antes de executar o código, é necessário configurar algumas informações da conta de email a ser consultada no arquivo <code>config.py</code>. As informações necessárias são:</p>
<ul><li><code>SERVER</code>: o servidor IMAP usado pela conta de email;</li><li><code>PORT</code>: a porta do servidor IMAP;</li><li><code>USERNAME</code>: o nome de usuário da conta de email;</li><li><code>PASSWORD</code>: a senha da conta de email.</li></ul>
<p>Certifique-se de que essas informações estejam corretas antes de executar o código.</p>
<p>As informações de configuração também podem ser fornecidas por meio de um arquivo JSON externo. O arquivo JSON deve ter a seguinte estrutura:</p>

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>json</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json"><span class="hljs-punctuation">{</span>
    <span class="hljs-attr">"SERVER"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"imap.gmail.com"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"PORT"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">993</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"USERNAME"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"seu_email@gmail.com"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"PASSWORD"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"sua_senha"</span>
<span class="hljs-punctuation">}</span>
</code></div></div></pre>
<p>O nome do arquivo JSON deve ser especificado na variável <code>enviro</code> no arquivo <code>main.py</code>. Caso contrário, o código usará as informações de configuração no arquivo <code>config.py</code>.</p>
<p>Além disso, é necessário instalar as bibliotecas <code>imaplib</code> e <code>win10toast</code>. Isso pode ser feito com o comando <code>pip install imaplib win10toast</code>.</p>

## Uso

<p>Para usar o código, execute o arquivo <code>main.py</code>. O código fará a busca por novas mensagens e exibirá as informações relevantes na tela e notificará o desktop para cada mensagem encontrada. Certifique-se de que o desktop está configurado para receber notificações do sistema operacional.</p>
<p>O código pode ser facilmente adaptado para usar outras palavras-chave e configurações de busca diferentes, basta modificar o arquivo <code>config.py</code> e o código em <code>main.py</code>.</p>


## Contribuição

<p>Sinta-se à vontade para contribuir com o projeto, fazendo sugestões, relatórios de bugs ou enviando pull requests.</p>

## Licença

<p>Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE.md para detalhes.</p>