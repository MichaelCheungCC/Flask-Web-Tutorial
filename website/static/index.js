// delete note
function deleteNote(noteID) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteID: noteID }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

// delete to-do
function deleteToDo(todoID) {
    fetch('/delete-to-do', {
        method: 'POST',
        body: JSON.stringify({ todoID: todoID }),
    }).then((_res) => {
        window.location.href = "/to-do";
    });
}

// jQuery to set active navigation bar
$(document).ready(function () {
    $('a[href="' + this.location.pathname + '"]').addClass("active");
});

// control the badge color based on category
const badgeColors = {
    'Personal': 'badge-primary',
    'Work': 'badge-success',
    'Study': 'badge-info',
    'Other': 'badge-secondary'
};
const categoryBadges = document.querySelectorAll('.category-badge');

function setBadgeColor(category, element) {
    const color = badgeColors[category] || 'badge-secondary';
    element.classList.add(color);
};

categoryBadges.forEach((categoryBadge) => {
    const category = categoryBadge.getAttribute('data-category');
    setBadgeColor(category, categoryBadge);
});