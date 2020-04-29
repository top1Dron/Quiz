$(document).ready ( function(){
    $("#id_email").change(function () {
        var eMail = $(this).val();
    
        $.ajax({
            url: 'ajax/validate_email/',
            data: {
                'email': eMail
            },
            dataType: 'json',
            success: function(data){
                if (data.is_taken){
                    alert('Користувач з ціє поштою вже існує.');
                }
            }
        });
    });

    var element = document.getElementById('id_group');
    if (element){
        document.getElementById("id_group").required = true;
    } else {
        document.getElementById("id_faculty").required = true;
        document.getElementById("id_cathedra").required = true;
    }
});