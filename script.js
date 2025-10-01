document.addEventListener('DOMContentLoaded', () => {
    // Play audio automatically
    const audio = document.querySelector('audio');
    if (audio) {
        audio.volume = 0.5; // Set volume to 50%
        audio.play().catch((error) => {
            console.error('Audio playback failed:', error);
        });
    }

    // Add hover effect to images
    const images = document.querySelectorAll('.box img');
    images.forEach((img) => {
        img.addEventListener('mouseover', () => {
            img.style.transform = 'scale(1.1)';
            img.style.transition = 'transform 0.3s ease-in-out';
        });
        img.addEventListener('mouseout', () => {
            img.style.transform = 'scale(1)';
        });
    });

    // Add click event to the button
    const button = document.querySelector('.button');
    if (button) {
        button.addEventListener('click', () => {
            alert('Thank you for clicking! ❤️');
        });
    }

    // Toggle visibility of the bottom text
    const bottomText = document.querySelector('.text-bottom');
    if (bottomText) {
        bottomText.style.cursor = 'pointer';
        bottomText.addEventListener('click', () => {
            bottomText.classList.toggle('hidden');
        });
    }
});