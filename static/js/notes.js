;(function() {

    $(document).ready(function() {
        $('.describe .like').click(function() {
            $(this).toggleClass('active');
        });

        $('#id_image').addClass('custom-file-input');

        $('#id_photo').addClass('custom-file-input');
    });
})();