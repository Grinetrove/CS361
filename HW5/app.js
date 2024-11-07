


document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowLeft') {
        window.history.back();
    } else if (event.key === 'ArrowRight') {
        window.history.forward();
    }
});


function confirmDelete() {
    const confirmation = confirm("Are you sure? This action is not reversible.");
    if (confirmation) {
        // Proceed with deletion logic (e.g., remove the row or make a delete request)
        alert("Item deleted successfully!"); // Placeholder action
    } else {
        // Deletion cancelled
        alert("Deletion canceled.");
    }
}


function takePhoto() {
    alert("Take Photo feature coming soon!");
}

function uploadDocument() {
    alert("Upload Document feature coming soon!");
}