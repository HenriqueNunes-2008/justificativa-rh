export async function buscarJustificativa(id) {

    const resposta = await fetch(`/api/justificativa/${id}`);

    if (!resposta.ok) {
        throw new Error("Erro ao carregar justificativa.");
    }

    return await resposta.json();
}


export async function excluirJustificativa(id) {

    const resposta = await fetch(
        `/api/justificativa/${id}/excluir`,
        {
            method: "DELETE"
        }
    );

    const dados = await resposta.json();

    if (!resposta.ok || !dados.success) {
        throw new Error(dados.message);
    }

    return dados;
}