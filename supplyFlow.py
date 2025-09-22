import time
import tkinter as tk
import random

COR_FUNDO_PRIMARIA = "#2c3e50"
COR_FUNDO_SECUNDARIA = "#34495e"
AZUL_PRIMARIO = "#3498db"
AZUL_DESTAQUE = "#2980b9"
COR_TEXTO = "#ecf0f1"
COR_HOVER_BTN = "#1abc9c"
VERDE_SUCESSO = "#27ae60"
VERMELHO_AVISO = "#e74c3c"
FUNDO_ENTRADA = "#ffffff"
TEXTO_ENTRADA = "#2c3e50"


class DialogoPersonalizado:
    """Classe base para criar diálogos personalizados com o tema do sistema"""

    def __init__(self, pai, titulo, mensagem, tipo_dialogo="info"):
        self.resultado = None
        self.pai = pai
        self.janela_dialogo = tk.Toplevel(pai)
        self.janela_dialogo.title(titulo)
        self.janela_dialogo.geometry("450x280")
        self.janela_dialogo.configure(bg=COR_FUNDO_PRIMARIA)
        self.janela_dialogo.resizable(False, False)
        self.janela_dialogo.transient(pai)
        self.janela_dialogo.grab_set()
        self.centralizar_janela()
        self.criar_interface(titulo, mensagem, tipo_dialogo)

    def centralizar_janela(self):
        """Centraliza a janela do diálogo"""
        self.janela_dialogo.update_idletasks()
        x = (self.janela_dialogo.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.janela_dialogo.winfo_screenheight() // 2) - (280 // 2)
        self.janela_dialogo.geometry(f"450x280+{x}+{y}")

    def criar_interface(self, titulo, mensagem, tipo_dialogo):
        """Cria a interface do diálogo"""
        cabecalho = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_SECUNDARIA, height=70)
        cabecalho.pack(fill=tk.X)
        cabecalho.pack_propagate(False)
        icones = {"info": "ℹ️", "success": "✅", "warning": "⚠️", "error": "❌", "question": "❓"}
        icone_label = tk.Label(
            cabecalho,
            text=icones.get(tipo_dialogo, "ℹ️"),
            font=("Segoe UI", 24),
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO
        )
        icone_label.pack(side=tk.LEFT, padx=25, pady=20)
        titulo_label = tk.Label(
            cabecalho,
            text=titulo,
            font=("Segoe UI", 16, "bold"),
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO
        )
        titulo_label.pack(side=tk.LEFT, pady=20)
        corpo_mensagem = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_PRIMARIA)
        corpo_mensagem.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        mensagem_label = tk.Label(
            corpo_mensagem,
            text=mensagem,
            font=("Segoe UI", 12),
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO,
            wraplength=380,
            justify=tk.LEFT
        )
        mensagem_label.pack()
        self.criar_botoes()

    def criar_botoes(self):
        pass

    def criar_botao(self, pai, texto, comando, cor_fundo=AZUL_PRIMARIO):
        """Cria um botão estilizado"""
        botao = tk.Button(
            pai,
            text=texto,
            font=("Segoe UI", 11, "bold"),
            bg=cor_fundo,
            fg=COR_TEXTO,
            activebackground=AZUL_DESTAQUE,
            activeforeground=COR_TEXTO,
            border=0,
            highlightthickness=0,
            padx=25,
            pady=10,
            relief="flat",
            cursor="hand2",
            command=comando,
            width=12
        )
        def ao_entrar(e):
            botao.config(bg=AZUL_DESTAQUE if cor_fundo == AZUL_PRIMARIO else "#c0392b")
        def ao_sair(e):
            botao.config(bg=cor_fundo)
        botao.bind("<Enter>", ao_entrar)
        botao.bind("<Leave>", ao_sair)
        return botao


class CaixaMensagemPersonalizada(DialogoPersonalizado):
    """Diálogo personalizado para exibir mensagens com barra de rolagem."""

    def __init__(self, pai, titulo, mensagem, tipo_dialogo="info"):
        self.mensagem = mensagem
        super().__init__(pai, titulo, mensagem, tipo_dialogo)
        self.janela_dialogo.wait_window()

    def criar_interface(self, titulo, mensagem, tipo_dialogo):
        cabecalho = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_SECUNDARIA, height=70)
        cabecalho.pack(fill=tk.X)
        cabecalho.pack_propagate(False)
        icones = {"info": "ℹ️", "success": "✅", "warning": "⚠️", "error": "❌", "question": "❓"}
        tk.Label(
            cabecalho,
            text=icones.get(tipo_dialogo, "ℹ️"),
            font=("Segoe UI", 24),
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO
        ).pack(side=tk.LEFT, padx=25, pady=20)
        tk.Label(
            cabecalho,
            text=titulo,
            font=("Segoe UI", 16, "bold"),
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO
        ).pack(side=tk.LEFT, pady=20)
        conteudo = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_PRIMARIA)
        conteudo.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        canvas = tk.Canvas(conteudo, bg=COR_FUNDO_PRIMARIA, highlightthickness=0)
        barra = tk.Scrollbar(conteudo, orient="vertical", command=canvas.yview)
        quadro_scroll = tk.Frame(canvas, bg=COR_FUNDO_PRIMARIA)
        quadro_scroll.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=quadro_scroll, anchor="nw")
        canvas.configure(yscrollcommand=barra.set)
        canvas.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        tk.Label(
            quadro_scroll,
            text=self.mensagem,
            font=("Segoe UI", 12),
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO,
            justify="left",
            wraplength=400
        ).pack()
        self.criar_botoes()

    def criar_botoes(self):
        frame_botoes = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_PRIMARIA)
        frame_botoes.pack(pady=(0, 20))
        ok_btn = self.criar_botao(frame_botoes, "OK", self.clique_ok)
        ok_btn.pack()
        ok_btn.focus_set()
        self.janela_dialogo.bind("<Return>", lambda e: self.clique_ok())
        self.janela_dialogo.bind("<Escape>", lambda e: self.clique_ok())

    def clique_ok(self):
        self.janela_dialogo.destroy()


class DialogoEntradaPersonalizado(DialogoPersonalizado):
    """Diálogo personalizado para entrada de texto"""

    def __init__(self, pai, titulo, pergunta, tipo_entrada="string"):
        self.pergunta = pergunta
        self.tipo_entrada = tipo_entrada
        self.campo_entrada = None
        self.rotulo_erro = None
        super().__init__(pai, titulo, pergunta, "question")
        self.janela_dialogo.wait_window()

    def criar_interface(self, titulo, mensagem, tipo_dialogo):
        cabecalho = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_SECUNDARIA, height=70)
        cabecalho.pack(fill=tk.X)
        cabecalho.pack_propagate(False)
        icone_label = tk.Label(
            cabecalho,
            text="❓",
            font=("Segoe UI", 24),
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO
        )
        icone_label.pack(side=tk.LEFT, padx=25, pady=20)
        titulo_label = tk.Label(
            cabecalho,
            text=titulo,
            font=("Segoe UI", 16, "bold"),
            bg=COR_FUNDO_SECUNDARIA,
            fg=COR_TEXTO
        )
        titulo_label.pack(side=tk.LEFT, pady=20)
        frame_entrada = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_PRIMARIA)
        frame_entrada.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        pergunta_label = tk.Label(
            frame_entrada,
            text=self.pergunta,
            font=("Segoe UI", 12),
            bg=COR_FUNDO_PRIMARIA,
            fg=COR_TEXTO,
            wraplength=380
        )
        pergunta_label.pack(anchor=tk.W, pady=(0, 15))
        self.campo_entrada = tk.Entry(
            frame_entrada,
            font=("Segoe UI", 13),
            bg=FUNDO_ENTRADA,
            fg=TEXTO_ENTRADA,
            relief="flat",
            bd=0,
            highlightthickness=2,
            highlightcolor=AZUL_PRIMARIO,
            highlightbackground="#bdc3c7"
        )
        self.campo_entrada.pack(fill=tk.X, ipady=10)
        self.campo_entrada.focus_set()
        self.frame_erro = tk.Frame(frame_entrada, bg=COR_FUNDO_PRIMARIA)
        self.frame_erro.pack(fill=tk.X, pady=(10, 0))
        self.criar_botoes()

    def criar_botoes(self):
        frame_botoes = tk.Frame(self.janela_dialogo, bg=COR_FUNDO_PRIMARIA)
        frame_botoes.pack(pady=(0, 25))
        ok_btn = self.criar_botao(frame_botoes, "OK", self.clique_ok)
        cancelar_btn = self.criar_botao(frame_botoes, "Cancelar", self.clique_cancelar, VERMELHO_AVISO)
        cancelar_btn.pack(side=tk.RIGHT, padx=(15, 0))
        ok_btn.pack(side=tk.RIGHT)
        self.janela_dialogo.bind("<Return>", lambda e: self.clique_ok())
        self.janela_dialogo.bind("<Escape>", lambda e: self.clique_cancelar())

    def clique_ok(self):
        valor = self.campo_entrada.get().strip()
        if not valor:
            self.exibir_erro("Por favor, insira um valor.")
            return
        if self.tipo_entrada == "integer":
            try:
                self.resultado = int(valor)
                if self.resultado <= 0:
                    self.exibir_erro("Por favor, insira um número positivo.")
                    return
            except ValueError:
                self.exibir_erro("Por favor, insira um número válido.")
                return
        else:
            self.resultado = valor
        self.janela_dialogo.destroy()

    def clique_cancelar(self):
        self.resultado = None
        self.janela_dialogo.destroy()

    def exibir_erro(self, mensagem):
        if self.rotulo_erro:
            self.rotulo_erro.destroy()
        self.rotulo_erro = tk.Label(
            self.frame_erro,
            text=f"⚠️ {mensagem}",
            font=("Segoe UI", 10),
            fg=VERMELHO_AVISO,
            bg=COR_FUNDO_PRIMARIA
        )
        self.rotulo_erro.pack(anchor=tk.W, pady=(5, 0))
        self.campo_entrada.focus_set()


def criar_botao_moderno(pai, texto, comando, cor_fundo=AZUL_PRIMARIO):
    botao = tk.Button(
        pai,
        text=texto,
        font=("Segoe UI", 12, "bold"),
        bg=cor_fundo,
        fg=COR_TEXTO,
        activebackground=COR_HOVER_BTN,
        activeforeground=COR_TEXTO,
        border=0,
        highlightthickness=0,
        padx=20,
        pady=12,
        relief="flat",
        cursor="hand2",
        command=comando
    )
    def ao_entrar(e):
        botao.config(bg=AZUL_DESTAQUE if cor_fundo == AZUL_PRIMARIO else "#c0392b")
    def ao_sair(e):
        botao.config(bg=cor_fundo)
    botao.bind("<Enter>", ao_entrar)
    botao.bind("<Leave>", ao_sair)
    return botao


def exibir_info(pai, titulo, mensagem):
    CaixaMensagemPersonalizada(pai, titulo, mensagem, "info")


def exibir_sucesso(pai, titulo, mensagem):
    CaixaMensagemPersonalizada(pai, titulo, mensagem, "success")


def exibir_aviso(pai, titulo, mensagem):
    CaixaMensagemPersonalizada(pai, titulo, mensagem, "warning")


def exibir_erro(pai, titulo, mensagem):
    CaixaMensagemPersonalizada(pai, titulo, mensagem, "error")


def perguntar_string(pai, titulo, pergunta):
    dialogo = DialogoEntradaPersonalizado(pai, titulo, pergunta, "string")
    return dialogo.resultado


def perguntar_inteiro(pai, titulo, pergunta):
    dialogo = DialogoEntradaPersonalizado(pai, titulo, pergunta, "integer")
    return dialogo.resultado


def logo_supplyflow():
    logo = r"""
███████╗██╗   ██╗██████╗ ██████╗ ██╗   ███╗   ███
██╔════╝██║   ██║██╔══██╗██╔══██╗██║    ███╗ ███
███████╗██║   ██║██████╔╝██████╔╝██║      ████╔╝
╚════██║██║   ██║██╔═══╝ ██╔═══╝ ██║       ██╔╝
███████║╚██████╔╝██║     ██║     ███████╗  ██║
╚══════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝  ╚═╝
███████╗██╗      █████╗ ██╗    ██╗
██╔════╝██║     ██╔══██╗██║    ██║
█████╗  ██║     ██║  ██║██║ █╗ ██║
██╔══╝  ██║     ██║  ██║██║███╗██║
██║     ███████╗ █████╔╝╚███╔███╔╝
╚═╝     ╚══════╝ ╚════╝  ╚══╝╚══╝        
𝗢 𝗴𝗲𝗿𝗲𝗻𝗰𝗶𝗮𝗺𝗲𝗻𝘁𝗼 𝗱𝗲 𝗲𝘀𝘁𝗼𝗾𝘂𝗲 𝗻𝗼 𝗺𝗮𝗶𝘀 𝗮𝗹𝘁𝗼 𝗻í𝘃𝗲𝗹!
"""
    raiz = tk.Tk()
    raiz.title("SupplyFlow - Sistema de Estoque")
    raiz.geometry("800x600")
    raiz.configure(bg=COR_FUNDO_PRIMARIA)
    raiz.resizable(False, False)
    raiz.eval('tk::PlaceWindow . center')
    label_logo = tk.Label(
        raiz,
        text=logo,
        font=("Consolas", 8, "bold"),
        fg=AZUL_PRIMARIO,
        bg=COR_FUNDO_PRIMARIA,
        justify="center"
    )
    label_logo.pack(pady=(50, 20))
    label_slogan = tk.Label(
        raiz,
        text="O gerenciamento de estoque no mais alto nível!",
        font=("Segoe UI", 16, "bold"),
        fg=COR_TEXTO,
        bg=COR_FUNDO_PRIMARIA
    )
    label_slogan.pack(pady=(0, 30))
    frame_progresso = tk.Frame(raiz, bg=COR_FUNDO_PRIMARIA)
    frame_progresso.pack(pady=20)
    label_carregando = tk.Label(
        frame_progresso,
        text="Carregando sistema...",
        font=("Segoe UI", 12),
        fg=COR_TEXTO,
        bg=COR_FUNDO_PRIMARIA
    )
    label_carregando.pack()
    raiz.after(3000, raiz.destroy)
    raiz.mainloop()


class Insumo:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __repr__(self):
        return f"{self.nome}: {self.quantidade}"


class Prateleira:
    def __init__(self, id):
        self.id = id
        self.insumos = {}

    def adicionar_insumo(self, nome, quantidade):
        if nome in self.insumos:
            self.insumos[nome].quantidade += quantidade
        else:
            self.insumos[nome] = Insumo(nome, quantidade)

    def exibir_estoque(self):
        resultado = f"\n{self.id}:\n"
        if self.insumos:
            for insumo in self.insumos.values():
                resultado += f"• {insumo}\n"
        else:
            resultado += "Estoque vazio.\n"
        return resultado


class SistemaEstoque:
    def __init__(self):
        self.estoque = {
            f"Prateleira_{i}": Prateleira(f"Prateleira_{i}") for i in range(1, 6)
        }
        self.lista_insumos = []
        self.historico_saidas = {}
        self.fila_consumo = [] 
        self.pilha_consumo = []   
        self._cadastrar_inicial("Seringas", 1000, "Prateleira_1")
        self._cadastrar_inicial("Luvas", 150, "Prateleira_1")
        self._cadastrar_inicial("Frascos de Vidro", 50, "Prateleira_2")
        self._cadastrar_inicial("Agulhas", 5000, "Prateleira_2")
        self._cadastrar_inicial("Álcool", 30, "Prateleira_3")
        self._cadastrar_inicial("Papel", 100, "Prateleira_4")
        self._cadastrar_inicial("Máscaras", 400, "Prateleira_5")

    def _cadastrar_inicial(self, nome, qtd, id_prateleira):
        self.estoque[id_prateleira].adicionar_insumo(nome, qtd)
        self.lista_insumos.append(nome)
        algoritmo = random.choice([self.merge_sort, self.quick_sort])
        self.lista_insumos = algoritmo(self.lista_insumos)

    def merge_sort(self, lista):
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esquerda = self.merge_sort(lista[:meio])
        direita = self.merge_sort(lista[meio:])
        return self._merge(esquerda, direita)

    def _merge(self, esq, dir):
        resultado = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            if esq[i].lower() <= dir[j].lower():
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir[j])
                j += 1
        resultado.extend(esq[i:])
        resultado.extend(dir[j:])
        return resultado

    def quick_sort(self, lista):
        """Quick Sort in-place otimizado."""
        def _partition(arr, low, high):
            pivo_idx = random.randint(low, high)
            arr[pivo_idx], arr[high] = arr[high], arr[pivo_idx]
            pivot = arr[high].lower()
            i = low - 1
            for j in range(low, high):
                if arr[j].lower() <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def _quick_sort(arr, low, high):
            if low < high:
                pi = _partition(arr, low, high)
                _quick_sort(arr, low, pi - 1)
                _quick_sort(arr, pi + 1, high)

        _quick_sort(lista, 0, len(lista) - 1)
        return lista

    def busca_binaria(self, lista, alvo):
        inicio, fim = 0, len(lista) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if lista[meio].lower() == alvo.lower():
                return True
            elif lista[meio].lower() < alvo.lower():
                inicio = meio + 1
            else:
                fim = meio - 1
        return False

    def busca_sequencial_recursiva(self, lista, elemento, indice=0):
        if indice >= len(lista):
            return False
        if lista[indice].lower() == elemento.lower():
            return True
        return self.busca_sequencial_recursiva(lista, elemento, indice + 1)

    def exibir_lista_insumos(self, pai):
        if not self.lista_insumos:
            exibir_info(pai, "Insumos Cadastrados", "Nenhum insumo cadastrado no sistema.")
            return
        texto = "Lista de insumos cadastrados (em ordem alfabética):\n\n"
        for i, nome in enumerate(self.lista_insumos, 1):
            texto += f"{i}. {nome}\n"
        exibir_info(pai, "📋 Insumos Cadastrados", texto)

    def exibir_estoque_total(self, pai):
        resultado = "RELATÓRIO COMPLETO DO ESTOQUE\n" + "="*40 + "\n"
        total_items = 0
        for prateleira in self.estoque.values():
            resultado += prateleira.exibir_estoque()
            total_items += len(prateleira.insumos)
        resultado += f"\n📊 Total de tipos de insumos: {total_items}"
        exibir_info(pai, "📦 Estoque Total", resultado)

    def adicionar_mais_estoque(self, nome, quantidade):
        for prateleira in self.estoque.values():
            if nome in prateleira.insumos:
                prateleira.adicionar_insumo(nome, quantidade)
                return True
        return False

    def retirar_insumo(self, pai, nome, quantidade):
        data_hora = time.strftime("%d/%m %H:%M")
        for prateleira in self.estoque.values():
            if nome in prateleira.insumos:
                insumo = prateleira.insumos[nome]
                if insumo.quantidade >= quantidade:
                    insumo.quantidade -= quantidade
                    self._registrar_consumo(nome, quantidade, data_hora)
                    exibir_sucesso(
                        pai,
                        "✅ Retirada Realizada",
                        f"{quantidade} unidades de '{nome}' retiradas.\nEstoque restante: {insumo.quantidade}"
                    )
                    return
                else:
                    exibir_aviso(
                        pai,
                        "⚠️ Estoque Insuficiente",
                        f"Disponível: {insumo.quantidade} unidades\nSolicitado: {quantidade}"
                    )
                    return
        exibir_erro(pai, "❌ Item Não Encontrado", f"O insumo '{nome}' não foi localizado.")

    def _registrar_consumo(self, nome, quantidade, timestamp):
        """Registra um evento de consumo em fila e pilha."""
        evento = f"{timestamp} | {nome}: {quantidade}"
        self.fila_consumo.append(evento)   
        self.pilha_consumo.append(evento)   

    def exibir_consumo_cronologico(self, pai):
        if not self.fila_consumo:
            exibir_info(pai, "📋 Consumo Diário", "Nenhum consumo registrado.")
            return
        texto = "Consumo Diário (ordem cronológica):\n\n"
        for evt in self.fila_consumo:
            texto += f"• {evt}\n"
        exibir_info(pai, "📋 Consumo Diário", texto)

    def exibir_consumo_inverso(self, pai):
        if not self.pilha_consumo:
            exibir_info(pai, "📋 Consumo Inverso", "Nenhuma consulta registrada.")
            return
        texto = "Consumo (últimos consumos primeiro):\n\n"
        for i in range(len(self.pilha_consumo)-1, -1, -1):
            texto += f"• {self.pilha_consumo[i]}\n"
        exibir_info(pai, "📋 Consumo Inverso", texto)

    def popular_historico(self, data, nome, quantidade):
        if data not in self.historico_saidas:
            self.historico_saidas[data] = {}
        self.historico_saidas[data][nome] = self.historico_saidas[data].get(nome, 0) + quantidade

    def exibir_historico(self, pai):
        if not self.historico_saidas:
            exibir_info(pai, "📈 Histórico", "Nenhuma movimentação de saída foi registrada ainda.")
            return
        resultado = "HISTÓRICO DE SAÍDAS\n" + "="*30 + "\n\n"
        total_saidas = 0
        for data, itens in self.historico_saidas.items():
            resultado += f"📅 {data}:\n"
            for nome, qtd in itens.items():
                resultado += f"   • {nome}: {qtd} unidades\n"
                total_saidas += qtd
            resultado += "\n"
        resultado += f"📊 Total de itens retirados: {total_saidas}"
        exibir_info(pai, "📈 Histórico de Saídas", resultado)

    def checagem_periodica(self, pai):
        resultado = "CHECAGEM PERIÓDICA DE ESTOQUE\n" + "="*40 + "\n\n"
        itens_baixos = itens_ok = 0
        for prateleira in self.estoque.values():
            for insumo in prateleira.insumos.values():
                if insumo.quantidade <= 50:
                    resultado += f"❌ {insumo.nome} ({prateleira.id}): {insumo.quantidade} - REABASTECER\n"
                    itens_baixos += 1
                else:
                    resultado += f"🆗 {insumo.nome} ({prateleira.id}): {insumo.quantidade} - OK\n"
                    itens_ok += 1
        resultado += f"\n📊 RESUMO:\n• Estoque baixo: {itens_baixos}\n• Estoque OK: {itens_ok}"
        if itens_baixos > 0:
            exibir_aviso(pai, "⚠️ Atenção Requerida", resultado)
        else:
            exibir_sucesso(pai, "✅ Estoque Adequado", resultado)

    def buscar_insumo(self, pai, nome):
        tipo_busca = random.choice(['binaria', 'sequencial'])
        if tipo_busca == 'binaria':
            usado = 'Busca Binária'
            encontrado = self.busca_binaria(self.lista_insumos, nome)
        else:
            usado = 'Busca Sequencial Recursiva'
            encontrado = self.busca_sequencial_recursiva(self.lista_insumos, nome)

        if encontrado:
            for prateleira in self.estoque.values():
                if nome in prateleira.insumos:
                    qtd = prateleira.insumos[nome].quantidade
                    status = ("✅ Disponível" if qtd > 50 else
                              "⚠️ Estoque baixo" if qtd > 0 else
                              "❌ Esgotado")
                    exibir_sucesso(
                        pai,
                        f"🔍 Item Encontrado ({usado})",
                        f"Insumo: {nome}\nLocalização: {prateleira.id}\n"
                        f"Quantidade: {qtd}\nStatus: {status}\n\n"
                        f"Algoritmo: {usado}"
                    )
                    return True
        else:
            exibir_erro(
                pai,
                f"❌ Item Não Encontrado ({usado})",
                f"O insumo '{nome}' não está cadastrado.\n"
                f"Algoritmo: {usado}"
            )
            return False

    def prateleira_com_menos_insumos(self):
        menor, pr = float('inf'), None
        for p in self.estoque.values():
            total = sum(ins.quantidade for ins in p.insumos.values())
            if total < menor:
                menor, pr = total, p
        return pr

    def adicionar_insumo_novo(self, pai, nome, quantidade):
        prateleira = self.prateleira_com_menos_insumos()
        prateleira.adicionar_insumo(nome, quantidade)
        self.lista_insumos.append(nome)
        algoritmo = random.choice([self.merge_sort, self.quick_sort])
        self.lista_insumos = algoritmo(self.lista_insumos)
        exibir_sucesso(
            pai,
            "✅ Novo Insumo Cadastrado",
            f"'{nome}' adicionado.\nLocalização: {prateleira.id}\nQuantidade: {quantidade}"
        )


class Principal:
    def __init__(self, sistema):
        self.sistema = sistema
        self.raiz = tk.Tk()
        self.raiz.title("SupplyFlow - Sistema de Gestão de Estoque")
        self.raiz.geometry("600x700")
        self.raiz.configure(bg=COR_FUNDO_PRIMARIA)
        self.raiz.resizable(False, False)
        self.raiz.eval('tk::PlaceWindow . center')
        self.criar_interface()
        self.raiz.mainloop()

    def criar_interface(self):
        cabecalho = tk.Frame(self.raiz, bg=COR_FUNDO_SECUNDARIA, height=120)
        cabecalho.pack(fill=tk.X)
        cabecalho.pack_propagate(False)
        tk.Label(
            cabecalho,
            text="SupplyFlow",
            font=("Segoe UI", 28, "bold"),
            fg=AZUL_PRIMARIO,
            bg=COR_FUNDO_SECUNDARIA
        ).pack(pady=(25, 5))
        tk.Label(
            cabecalho,
            text="Sistema Moderno de Gestão de Estoque",
            font=("Segoe UI", 12),
            fg=COR_TEXTO,
            bg=COR_FUNDO_SECUNDARIA
        ).pack()
        quadro = tk.Frame(self.raiz, bg=COR_FUNDO_PRIMARIA)
        quadro.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        botoes = [
            ("📊 Exibir Estoque Total", lambda: self.sistema.exibir_estoque_total(self.raiz)),
            ("➕ Adicionar à Insumo Existente", self.adicionar_estoque),
            ("🆕 Cadastrar Novo Insumo", self.cadastrar_novo_insumo),
            ("➖ Retirar Insumo", self.retirar_insumo),
            ("🔍 Buscar Insumo", self.buscar_insumo),
            ("📋 Insumos Cadastrados", lambda: self.sistema.exibir_lista_insumos(self.raiz)),
            ("📈 Histórico de Saídas", lambda: self.sistema.exibir_historico(self.raiz)),
            ("🔔 Checagem Periódica", lambda: self.sistema.checagem_periodica(self.raiz)),
            ("🗒️ Consumo Cronológico", lambda: self.sistema.exibir_consumo_cronologico(self.raiz)),
            ("🔄 Consumo Inverso", lambda: self.sistema.exibir_consumo_inverso(self.raiz)),
            ("❌ Sair", self.raiz.quit),
        ]

        for txt, cmd in botoes:
            cor = VERMELHO_AVISO if "Sair" in txt else AZUL_PRIMARIO
            btn = criar_botao_moderno(quadro, txt, cmd, cor)
            btn.pack(fill=tk.X, pady=8)

    def adicionar_estoque(self):
        nome = perguntar_string(self.raiz, "Adicionar Estoque", "Nome do insumo:")
        if nome:
            qtd = perguntar_inteiro(self.raiz, "Quantidade", f"Quantas unidades de '{nome}'?")
            if qtd and self.sistema.adicionar_mais_estoque(nome, qtd):
                exibir_sucesso(self.raiz, "✅ Estoque Atualizado", f"{qtd} unidades adicionadas.")
            else:
                exibir_erro(self.raiz, "❌ Insumo Não Encontrado", "Cadastre como novo insumo.")

    def cadastrar_novo_insumo(self):
        nome = perguntar_string(self.raiz, "Novo Insumo", "Digite o nome do novo insumo:")
        if nome:
            qtd = perguntar_inteiro(self.raiz, "Quantidade Inicial", f"Quantidade inicial de '{nome}'?")
            if qtd:
                self.sistema.adicionar_insumo_novo(self.raiz, nome, qtd)

    def retirar_insumo(self):
        nome = perguntar_string(self.raiz, "Retirar Insumo", "Digite o nome do insumo:")
        if nome:
            qtd = perguntar_inteiro(self.raiz, "Quantidade", f"Quantas unidades de '{nome}'?")
            if qtd:
                self.sistema.retirar_insumo(self.raiz, nome, qtd)

    def buscar_insumo(self):
        nome = perguntar_string(self.raiz, "Buscar Insumo", "Digite o nome do insumo:")
        if nome:
            self.sistema.buscar_insumo(self.raiz, nome)


if __name__ == "__main__":
    logo_supplyflow()
    sistema = SistemaEstoque()
    Principal(sistema)
