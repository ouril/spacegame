function getData() {
    $(document).ready(
        function () {
            $.post('/', {text: 'Текст'}, function (data) {

                alert(data);

            });
        }
    )
}