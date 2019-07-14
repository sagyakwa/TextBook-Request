(function ($) {
    // USE STRICT
    "use strict";

    $(".form-radio .radio-item").click(function(){
        //Spot switcher:
        $(this).parent().find(".radio-item").removeClass("active");
        $(this).addClass("active");
    });
  
    $('#course_type').parent().append('<ul class="list-item" id="newcourse_type" name="course_type"></ul>');
    $('#course_type option').each(function(){
        $('#newcourse_type').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
    });
    $('#course_type').remove();
    $('#newcourse_type').attr('id', 'course_type');
    $('#course_type li').first().addClass('init');
    $("#course_type").on("click", ".init", function() {
        $(this).closest("#course_type").children('li:not(.init)').toggle('slow');
    });

    $('#confirm_type').parent().append('<ul class="list-item" id="newconfirm_type" name="confirm_type"></ul>');
    $('#confirm_type option').each(function(){
        $('#newconfirm_type').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
    });
    $('#confirm_type').remove();
    $('#newconfirm_type').attr('id', 'confirm_type');
    $('#confirm_type li').first().addClass('init');
    $("#confirm_type").on("click", ".init", function() {
        $(this).closest("#confirm_type").children('li:not(.init)').toggle('slow');
    });
})(jQuery);