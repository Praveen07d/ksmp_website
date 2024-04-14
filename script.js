document.addEventListener('DOMContentLoaded', function() {
    const playButton = document.getElementById('playButton');
    const popupCard = document.getElementById('popupCard');
    
    playButton.addEventListener('click', function() {
        const textToCopy = 'play.kanglasmp.me';
        
        const textarea = document.createElement('textarea');
        textarea.value = textToCopy;
        document.body.appendChild(textarea);
        
        textarea.select();
        document.execCommand('copy');
        
        document.body.removeChild(textarea);
        
        popupCard.classList.add('show');
        
        setTimeout(() => {
            popupCard.classList.remove('show');
        }, 2000);
    });
});
