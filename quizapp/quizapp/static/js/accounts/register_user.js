$(document).ready ( function(){
    $('#id_birthdate').datepicker();

    if ($('#id_isLecturer').attr("checked")) {
        $('#student').hide();
        $('#lecturer').show();
        document.getElementById("id_faculty").required = true;
        document.getElementById("id_cathedra").required = true;
        document.getElementById("id_group").required = false;
    } else {
        $('#student').show();
        $('#lecturer').hide();
        document.getElementById("id_faculty").required = false;
        document.getElementById("id_cathedra").required = false;
        document.getElementById("id_group").required = true;
    }
    
    $('#id_isLecturer').click(function() {
        $('#student')[this.checked ? "hide" : "show"]();
        if (this.checked) {
            document.getElementById("id_faculty").required = true;
            document.getElementById("id_cathedra").required = true;
            document.getElementById("id_group").required = false;
        }
        else {
            document.getElementById("id_faculty").required = false;
            document.getElementById("id_cathedra").required = false;
            document.getElementById("id_group").required = true;
        }
        $('#lecturer')[this.checked ? "show" : "hide"]();
    });

    $("#id_username").change(function () {
        var userName = $(this).val();
    
        $.ajax({
            url: 'ajax/validate_username/',
            data: {
                'username': userName
            },
            dataType: 'json',
            success: function(data){
                if (data.is_taken){
                    alert('Користувач з цим логіном вже існує.');
                }
            }
        });
    });

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
});