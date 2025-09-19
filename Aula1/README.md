## Automação de Cadastro de Produtos (PyAutoGUI)

Este projeto automatiza o login em um sistema web e o cadastro de produtos a partir de uma base CSV utilizando Python, PyAutoGUI e Pandas.

Esta aula faz parte da Jornada Python Power da Hashtag. Assista ao conteúdo relacionado no YouTube: [Jornada Python Power](https://www.youtube.com/watch?v=RqTDtsITYSM&t=5s).

### Estrutura
- `codigo.py`: script principal que abre o navegador, faz login, lê `produtos.csv` e cadastra cada produto na página.
- `auxiliar.py`: utilitário para capturar a posição do cursor do mouse (coordenadas x, y) após 5 segundos. Útil para ajustar `click(x=..., y=...)` no `codigo.py`.
- `produtos.csv`: base de dados com os produtos a serem cadastrados.

### Pré-requisitos
- Python 3.8+
- Dependências: `pyautogui`, `pandas`

Instalação das dependências:
```bash
pip install pyautogui pandas
```

No Windows, o PyAutoGUI pode requerer:
- `pip install pillow`
- Executar o script em modo que permita controle do mouse e teclado (sem bloqueios de tela)

### Uso
1. Abra o projeto na pasta `Aula1`.
2. Ajuste, se necessário, as coordenadas de clique no `codigo.py` usando `auxiliar.py`:
   - Execute `python auxiliar.py` e posicione o mouse onde deseja clicar; após 5s a posição é exibida no console.
3. Verifique/edite as credenciais no `codigo.py` e o caminho do CSV (`produtos.csv`).
4. Garanta que o navegador Microsoft Edge esteja instalado (o script abre via tecla Windows e pesquisa por "edge").
5. Execute o script principal:
```bash
python codigo.py
```

Durante a execução:
- Não utilize o computador, pois o PyAutoGUI controlará mouse e teclado.
- A janela do navegador deve permanecer em foco.

### CSV esperado (`produtos.csv`)
Colunas obrigatórias: `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`.

Observações:
- O campo `obs` é opcional; se estiver vazio, o script não digita `nan`.
- Certifique-se de que o separador é vírgula e o arquivo está na mesma pasta do script.

### Dicas e segurança
- Ajuste `pyautogui.PAUSE` no `codigo.py` se precisar desacelerar/acelerar.
- Execute em um ambiente controlado para evitar cliques indesejados.
- Para interromper rapidamente, mova o mouse para o canto superior esquerdo (fail-safe do PyAutoGUI) ou feche a janela do terminal.

### Licença
Uso educacional/demonstrativo.


