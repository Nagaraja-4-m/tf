function EditItem(item_id,cancel_btn_id){
    var item=document.getElementById(item_id);
        item.removeAttribute('disabled');
        document.getElementById(cancel_btn_id).style.display='flex';
    }

    function  DisableItem(item_id,cancel_btn_id){
        var item=document.getElementById(item_id);
        item.disabled = true;
        document.getElementById(cancel_btn_id).style.display='none';
    }