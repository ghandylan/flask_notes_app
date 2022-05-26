function deleteNote(noteId) {
    fetch('/delete-note',
    {   
        method: 'POST',
        body: JSON.stringify({  noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

// update note function
// Language: javascript
// Path: codes\public\python\flask_notes_crud\static\index.js
function updateNote(noteId) {
    fetch('/update-note',
    {   
        method: 'POST',
        body: JSON.stringify({  noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}