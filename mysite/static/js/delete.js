const deleteButtons = document.querySelectorAll('.delete-button');
deleteButtons.forEach(button => {
  button.addEventListener('click', () => {

    const objectId = button.dataset.objectId;
    fetch('/delete/item', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': '{{ csrf_token }}'
      },
      body: `id=${objectId}`
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        button.parentNode.remove();
      } else {
        console.error(data.error);
      }
    })
    .catch(error => console.error(error));
  });
});