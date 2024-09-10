$(document).ready(function() {
    const alertBox = $('#alert');

    function showAlert(message, type) {
        alertBox.removeClass('success error').addClass(type).text(message).slideDown();
        setTimeout(() => {
            alertBox.slideUp();
        }, 3000);
    }

    function loadProducts() {
        fetch('/api/products/')
            .then(response => response.json())
            .then(data => {
                let tableBody = $('#productTable tbody');
                tableBody.empty();
                data.forEach(product => {
                    tableBody.append(
                        `<tr>
                            <td>${product.id}</td>
                            <td>${product.name}</td>
                            <td>${product.description}</td>
                            <td>${product.price}</td>
                        </tr>`
                    );
                });
            });
    }

    $('#productForm').submit(function(event) {
        event.preventDefault();
        const name = $('#name').val().trim();
        const description = $('#description').val().trim();
        const price = parseFloat($('#price').val());

        if (!name) {
            showAlert('The Name may not be blank', 'error');
            return;
        }
        if (price <= 0 || isNaN(price)) {
            showAlert('The Price must be a positive number', 'error');
            return;
        }

        const formData = {
            name: name,
            description: description,
            price: price
        };

        fetch('/api/products/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                return response.json().then(err => {
                    throw new Error(Object.values(err).join(', '));
                });
            }
        })
        .then(data => {
            showAlert('Product has been added', 'success');
            loadProducts();
            $('#productForm')[0].reset();
        })
        .catch(error => {
            showAlert(`Error: ${error.message}`, 'error');
        });
    });

    loadProducts();
});
