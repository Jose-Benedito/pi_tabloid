

function valida_form (){

    if(document.getElementById("estabelecimento").value == ""){
        alert('Por favor, marque o estabelecimento');
        document.getElementById("estabelecimento").focus();
        return false;
    }
    if(document.getElementById("tipo_item").value == ""){
        alert('Por favor, preencha o campo tipo do item');
        document.getElementById("tipo_item").focus();
        return false;
    }
    if(document.getElementById("nome_item").value == ""){
        alert('Por favor, preencha o campo nome do produto');
        document.getElementById("nome_item").focus();
        return false;
    }
    if(document.getElementById("marca_item").value == ""){
        alert('Por favor, preencha o campo marca');
        document.getElementById("marca_item").focus();
        return false;
    }
    if(document.getElementById("volume_tipo").value == ""){
        alert('Por favor, preencha o campo tipo da quantidade');
        document.getElementById("volume_tipo").focus();
        return false;
    }
    if(document.getElementById("volume").value == ""){
        alert('Por favor, preencha o campo quantidade');
        document.getElementById("volume").focus();
        return false;
    }
    if(document.getElementById("qtd_maxima").value == ""){
        alert('Por favor, preencha o campo quantidade máxima');
        document.getElementById("qtd_maxima").focus();
        return false;
    }
    if(document.getElementById("valor").value == ""){
        alert('Por favor, preencha o campo valor');
        document.getElementById("valor").focus();
        return false;
    }
    if(document.getElementById("foto").value == ""){
        alert('Por favor, preencha adicione uma foto do produto');
        document.getElementById("foto").focus();
        return false;
    }
    if(document.getElementById("data_fim_promocao").value == ""){
        alert('Por favor, preencha o campo data final da promoção');
        document.getElementById("data_fim_promocao").focus();
        return false;
    }
}