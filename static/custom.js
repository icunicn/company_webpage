/**
 * Custom JavaScript for company website
 * Handles navbar functionality and other site-specific behaviors
 */
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on blog page by looking for the class on body
    const isBlogPage = document.body.classList.contains('is-blog-page');
    
    // Initialize mobile navigation
    initMobileNav(isBlogPage);
    
    // Handle active states for navbar links
    highlightActiveNavLink();
    
    // Add smooth scrolling for anchor links
    enableSmoothScroll();
});

/**
 * Initialize mobile navigation with special handling for blog pages
 */
function initMobileNav(isBlogPage) {
    const mobileToggle = document.querySelectorAll('.mobile-nav-toggle');
    const navbar = document.querySelector('#navbar');
    
    mobileToggle.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            document.body.classList.toggle('mobile-nav-active');
            
            // Toggle between show/hide icons
            document.querySelector('.mobile-nav-show').classList.toggle('d-none');
            document.querySelector('.mobile-nav-hide').classList.toggle('d-none');
            
            // Add special class if we're on blog page
            if (isBlogPage) {
                navbar.classList.toggle('blog-mobile-active');
            }
        });
    });
    
    // Close mobile menu when clicking on a navigation link
    const navLinks = document.querySelectorAll('#navbar a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (document.body.classList.contains('mobile-nav-active')) {
                document.body.classList.remove('mobile-nav-active');
                document.querySelector('.mobile-nav-show').classList.remove('d-none');
                document.querySelector('.mobile-nav-hide').classList.add('d-none');
                
                if (isBlogPage) {
                    navbar.classList.remove('blog-mobile-active');
                }
            }
        });
    });
}

/**
 * Highlight active navigation link based on current section
 */
function highlightActiveNavLink() {
    const navLinks = document.querySelectorAll('#navbar a');
    
    // Only process links with hash (section links)
    navLinks.forEach(link => {
        if (!link.hash) return;
        
        const section = document.querySelector(link.hash);
        if (!section) return;
        
        // Add scroll event to highlight active link
        window.addEventListener('scroll', function() {
            const position = window.scrollY + 200;
            
            if (position >= section.offsetTop && 
                position <= (section.offsetTop + section.offsetHeight)) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    });
}

/**
 * Enable smooth scrolling for anchor links
 */
function enableSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            // Skip if it's just a "#" link
            if (this.getAttribute('href') === '#') return;
            
            const target = document.querySelector(this.getAttribute('href'));
            if (!target) return;
            
            e.preventDefault();
            
            window.scrollTo({
                top: target.offsetTop - 70, // Offset for fixed header
                behavior: 'smooth'
            });
        });
    });
}
```
