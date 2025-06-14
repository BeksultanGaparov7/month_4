// Smooth scrolling for navigation
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// CTA Button Animation
const ctaButton = document.getElementById('cta-button');
ctaButton.addEventListener('click', () => {
    alert("Thank you for your interest! We'll contact you soon.");
});

// Dynamic year in footer (optional)
document.getElementById('year').textContent = new Date().getFullYear();

document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (e) => {
        console.log("Link clicked:", e.target.href);
    });
});