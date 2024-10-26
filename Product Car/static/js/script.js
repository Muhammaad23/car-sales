document.querySelectorAll('.car').forEach(item => {
    item.addEventListener('mouseover', () => {
        // Example hover effect code, like showing additional details
        item.style.borderColor = "#007bff";
    });

    item.addEventListener('mouseout', () => {
        item.style.borderColor = "#ddd";
    });
});