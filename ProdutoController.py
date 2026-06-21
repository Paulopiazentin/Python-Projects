from services.database import conectar
from Models.ProdutoPerecivel import ProdutoPerecivel
from Models.ProdutoDuravel import ProdutoDuravel

from Models.Categoria import Categoria
from Models.Fornecedor import Fornecedor
from Models.Movimentacao import Movimentacao
from datetime import date
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# CATEGORIA
# ═══════════════════════════════════════════════════════════════════════════════

def listar_categorias() -> list[Categoria]:
    with conectar() as conn:
        rows = conn.execute(
            "SELECT * FROM categoria ORDER BY nome_categoria"
        ).fetchall()
    return [Categoria(r["id_categoria"], r["nome_categoria"]) for r in rows]


def incluir_categoria(nome: str) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            conn.execute(
                "INSERT INTO categ oria (nome_categoria) VALUES (?)", (nome,)
            )
        return True, "Categoria cadastrada!"
    except Exception as e:
        return False, str(e)


def excluir_categoria(id_cat: int) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            conn.execute(
                "DELETE FROM categoria WHERE id_categoria = ?", (id_cat,)
            )
        return True, "Categoria excluída!"
    except Exception as e:
        return False, str(e)


# ═══════════════════════════════════════════════════════════════════════════════
# FORNECEDOR
# ═══════════════════════════════════════════════════════════════════════════════

def listar_fornecedores() -> list[Fornecedor]:
    with conectar() as conn:
        rows = conn.execute(
            "SELECT * FROM fornecedor ORDER BY nome"
        ).fetchall()
    return [Fornecedor(r["id_fornecedor"], r["nome"], r["telefone"], r["email"])
            for r in rows]


def incluir_fornecedor(nome: str, telefone: str, email: str) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            conn.execute(
                "INSERT INTO fornecedor (nome, telefone, email) VALUES (?,?,?)",
                (nome, telefone, email)
            )
        return True, "Fornecedor cadastrado!"
    except Exception as e:
        return False, str(e)


def excluir_fornecedor(id_forn: int) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            conn.execute(
                "DELETE FROM fornecedor WHERE id_fornecedor = ?", (id_forn,)
            )
        return True, "Fornecedor excluído!"
    except Exception as e:
        return False, str(e)


def vincular_produto_fornecedor(id_produto: int, id_fornecedor: int) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            conn.execute(
                "INSERT OR IGNORE INTO produto_fornecedor VALUES (?,?)",
                (id_produto, id_fornecedor)
            )
        return True, "Vínculo criado!"
    except Exception as e:
        return False, str(e)


def fornecedores_do_produto(id_produto: int) -> list[Fornecedor]:
    with conectar() as conn:
        rows = conn.execute("""
            SELECT f.* FROM fornecedor f
            JOIN produto_fornecedor pf ON f.id_fornecedor = pf.id_fornecedor
            WHERE pf.id_produto = ?
        """, (id_produto,)).fetchall()
    return [Fornecedor(r["id_fornecedor"], r["nome"], r["telefone"], r["email"])
            for r in rows]


# ═══════════════════════════════════════════════════════════════════════════════
# PRODUTO
# ═══════════════════════════════════════════════════════════════════════════════

def _row_to_produto(r):
    if r["tipo"] == "Perecível":
        return ProdutoPerecivel(
            r["id_produto"], r["nome"], r["descricao"] or "",
            r["preco"], r["quantidade"], r["id_categoria"],
            r["validade"] or "", r["lote"] or ""
        )
    return ProdutoDuravel(
        r["id_produto"], r["nome"], r["descricao"] or "",
        r["preco"], r["quantidade"], r["id_categoria"],
        r["garantia_meses"] or 0, r["fabricante"] or ""
    )


def listar_produtos(tipo: Optional[str] = None,
                    id_categoria: Optional[int] = None) -> list:
    sql = "SELECT * FROM produto WHERE 1=1"
    params: list = []
    if tipo:
        sql += " AND tipo = ?"
        params.append(tipo)
    if id_categoria:
        sql += " AND id_categoria = ?"
        params.append(id_categoria)
    sql += " ORDER BY nome"
    with conectar() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [_row_to_produto(r) for r in rows]


def buscar_produto(id_produto: int) -> Optional[object]:
    with conectar() as conn:
        row = conn.execute(
            "SELECT * FROM produto WHERE id_produto = ?", (id_produto,)
        ).fetchone()
    return _row_to_produto(row) if row else None


def incluir_produto(produto) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            if isinstance(produto, ProdutoPerecivel):
                conn.execute("""
                    INSERT INTO produto
                        (nome, descricao, preco, quantidade, id_categoria,
                         tipo, validade, lote)
                    VALUES (?,?,?,?,?,?,?,?)
                """, (
                    produto.get_nome(), produto.get_descricao(),
                    produto.get_preco(), produto.get_quantidade(),
                    produto.get_id_categoria(), produto.get_tipo(),
                    produto.get_validade(), produto.get_lote()
                ))
            else:
                conn.execute("""
                    INSERT INTO produto
                        (nome, descricao, preco, quantidade, id_categoria,
                         tipo, garantia_meses, fabricante)
                    VALUES (?,?,?,?,?,?,?,?)
                """, (
                    produto.get_nome(), produto.get_descricao(),
                    produto.get_preco(), produto.get_quantidade(),
                    produto.get_id_categoria(), produto.get_tipo(),
                    produto.get_garantia_meses(), produto.get_fabricante()
                ))
        return True, "Produto cadastrado com sucesso!"
    except Exception as e:
        return False, str(e)


def alterar_produto(dados: dict) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            conn.execute("""
                UPDATE produto
                SET nome=?, descricao=?, preco=?, quantidade=?, id_categoria=?,
                    validade=?, lote=?, garantia_meses=?, fabricante=?
                WHERE id_produto=?
            """, (
                dados["nome"], dados.get("descricao"),
                dados["preco"], dados["quantidade"], dados.get("id_categoria"),
                dados.get("validade"), dados.get("lote"),
                dados.get("garantia_meses"), dados.get("fabricante"),
                dados["id_produto"]
            ))
        return True, "Produto atualizado!"
    except Exception as e:
        return False, str(e)


def excluir_produto(id_produto: int) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            # Remove vínculos filhos antes para evitar FOREIGN KEY constraint
            conn.execute(
                "DELETE FROM produto_fornecedor WHERE id_produto = ?", (id_produto,)
            )
            conn.execute(
                "DELETE FROM movimentacao WHERE id_produto = ?", (id_produto,)
            )
            conn.execute(
                "DELETE FROM produto WHERE id_produto = ?", (id_produto,)
            )
        return True, "Produto excluído!"
    except Exception as e:
        return False, str(e)


def produtos_estoque_baixo(limite: int = 10) -> list:
    with conectar() as conn:
        rows = conn.execute(
            "SELECT * FROM produto WHERE quantidade <= ? ORDER BY quantidade",
            (limite,)
        ).fetchall()
    return [_row_to_produto(r) for r in rows]


# ═══════════════════════════════════════════════════════════════════════════════
# MOVIMENTAÇÃO
# ═══════════════════════════════════════════════════════════════════════════════

def registrar_movimentacao(id_produto: int, tipo: str,
                            quantidade: int) -> tuple[bool, str]:
    try:
        with conectar() as conn:
            row = conn.execute(
                "SELECT quantidade FROM produto WHERE id_produto = ?",
                (id_produto,)
            ).fetchone()
            if not row:
                return False, "Produto não encontrado."

            estoque = row["quantidade"]
            if tipo == "Saída" and quantidade > estoque:
                return False, f"Estoque insuficiente! Disponível: {estoque} un."

            novo = estoque + quantidade if tipo == "Entrada" else estoque - quantidade
            hoje = date.today().strftime("%d/%m/%Y")

            conn.execute("""
                INSERT INTO movimentacao (tipo, data, quantidade, id_produto)
                VALUES (?,?,?,?)
            """, (tipo, hoje, quantidade, id_produto))

            conn.execute(
                "UPDATE produto SET quantidade = ? WHERE id_produto = ?",
                (novo, id_produto)
            )
        return True, f"Movimentação registrada! Novo estoque: {novo} un."
    except Exception as e:
        return False, str(e)


def listar_movimentacoes(id_produto: Optional[int] = None) -> list[Movimentacao]:
    sql = """
        SELECT m.* FROM movimentacao m
        JOIN produto p ON m.id_produto = p.id_produto
    """
    params: list = []
    if id_produto:
        sql += " WHERE m.id_produto = ?"
        params.append(id_produto)
    sql += " ORDER BY m.id_movimentacao DESC"
    with conectar() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [
        Movimentacao(
            r["id_movimentacao"], r["tipo"], r["data"],
            r["quantidade"], r["id_produto"]
        ) for r in rows
    ]


def listar_movimentacoes_dict(id_produto: Optional[int] = None) -> list[dict]:
    sql = """
        SELECT m.*, p.nome AS produto_nome
        FROM movimentacao m
        JOIN produto p ON m.id_produto = p.id_produto
    """
    params: list = []
    if id_produto:
        sql += " WHERE m.id_produto = ?"
        params.append(id_produto)
    sql += " ORDER BY m.id_movimentacao DESC"
    with conectar() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


# ═══════════════════════════════════════════════════════════════════════════════
# STATS para Dashboard
# ═══════════════════════════════════════════════════════════════════════════════

def stats_por_categoria() -> list[dict]:
    with conectar() as conn:
        rows = conn.execute("""
            SELECT c.nome_categoria,
                   COUNT(p.id_produto)        AS total_produtos,
                   SUM(p.quantidade)          AS total_unidades,
                   SUM(p.preco * p.quantidade) AS valor_total
            FROM categoria c
            LEFT JOIN produto p ON c.id_categoria = p.id_categoria
            GROUP BY c.id_categoria
            ORDER BY valor_total DESC
        """).fetchall()
    return [dict(r) for r in rows]


def movimentacoes_por_dia(dias: int = 30) -> list[dict]:
    with conectar() as conn:
        rows = conn.execute("""
            SELECT data, tipo, SUM(quantidade) AS total
            FROM movimentacao
            GROUP BY data, tipo
            ORDER BY data
        """).fetchall()
    return [dict(r) for r in rows]
