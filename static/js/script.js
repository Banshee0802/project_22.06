document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('myAlertButton');
    const toastEl = document.getElementById('liveToast');

    if (button && toastEl) {
        const toast = new bootstrap.Toast(toastEl);

        button.addEventListener('click', function () {
            toast.show();
        });
    }
});