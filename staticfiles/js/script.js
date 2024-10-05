function scrollLeft() {
    const galleryGrid = document.querySelector('.gallery-grid');
    galleryGrid.scrollBy({ left: -300, behavior: 'smooth' });
}

function scrollRight() {
    const galleryGrid = document.querySelector('.gallery-grid');
    galleryGrid.scrollBy({ left: 300, behavior: 'smooth' });
}

document.querySelectorAll('.clickable-stars').forEach(starContainer => {
starContainer.addEventListener('click', function(e) {
    const starIndex = Array.from(this.children).indexOf(e.target) + 1;
    this.dataset.rating = starIndex;
    updateStars(this, starIndex);
});
});

function updateStars(container, rating) {
Array.from(container.children).forEach((star, index) => {
    if (index < rating) {
        star.classList.add('active');
    } else {
        star.classList.remove('active');
    }
});
}

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.navigation-tabs button');
    const sections = document.querySelectorAll('section');
    const navBar = document.querySelector('.navigation-tabs');

    // Ensure buttons and sections exist before adding event listeners
    if (buttons.length > 0 && sections.length > 0 && navBar) {
        // Smooth scroll when clicking on a navigation button
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons
                buttons.forEach(btn => btn.classList.remove('active'));

                // Add active class to the clicked button
                button.classList.add('active');

                // Get the target section ID
                const targetId = button.getAttribute('data-target');
                const targetSection = document.getElementById(targetId);

                if (targetSection) {
                    // Scroll to the targeted section smoothly
                    targetSection.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Track the active section as the user scrolls
        window.addEventListener('scroll', () => {
            let currentSection = '';

            sections.forEach(section => {
                const sectionTop = section.offsetTop - 100; // Adjust for any padding/margin around sections
                if (pageYOffset >= sectionTop) {
                    currentSection = section.getAttribute('id');
                }
            });

            // Update the active button based on the current section
            buttons.forEach(button => {
                button.classList.remove('active');
                if (button.getAttribute('data-target') === currentSection) {
                    button.classList.add('active');
                }
            });

            // Make the navigation sticky if the user scrolls past it
            const navTop = navBar.offsetTop;
            if (window.scrollY >= navTop) {
                navBar.classList.add('sticky');
            } else {
                navBar.classList.remove('sticky');
            }
        });

        // Set a default active tab when the page loads
        document.querySelector('.navigation-tabs button').click();
    } else {
        console.error("Navigation tabs, buttons, or sections are missing from the DOM.");
    }
});


function toggleText() {
    var aboutText = document.getElementById("aboutText");
    var moreText = document.getElementById("moreText");
    var toggleButton = document.getElementById("toggleButton");

    if (aboutText.classList.contains("expanded")) {
        aboutText.classList.remove("expanded");
        moreText.classList.add("hidden");
        toggleButton.textContent = "Read More...";
    } else {
        aboutText.classList.add("expanded");
        moreText.classList.remove("hidden");
        toggleButton.textContent = "Read Less";
    }
}
function toggleChatBox() {
    const chatBox = document.getElementById("chatBox");
    chatBox.style.display = chatBox.style.display === "flex" ? "none" : "flex";
}
// Function to send a message
function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const messageContent = messageInput.value.trim();
    
    if (messageContent) {
        const chatBody = document.getElementById("chatBody");
  
      // Create a new message div
        const newMessage = document.createElement("div");
        newMessage.classList.add("message", "sent");
  
      // Message content
        const messageText = document.createElement("div");
        messageText.classList.add("message-content");
        messageText.textContent = messageContent;
  
      // Timestamp
        const timestamp = document.createElement("div");
        timestamp.classList.add("timestamp");
        const now = new Date();
        timestamp.textContent = `${now.getHours()}:${now.getMinutes()}`;
  
      // Append elements
        newMessage.appendChild(messageText);
        newMessage.appendChild(timestamp);
        chatBody.appendChild(newMessage);
  
      // Clear input field
        messageInput.value = "";
  
      // Scroll to bottom of chat
        chatBody.scrollTop = chatBody.scrollHeight;
    }
}
  

// Function to display the rating value beside the stars
const overallStars = document.querySelectorAll('input[name="rating"]');
const overallRatingValue = document.getElementById('overall-rating-value');

overallStars.forEach(star => {
    star.addEventListener('change', () => {
        overallRatingValue.textContent = star.value;
    });
});

// Repeat the same logic for other star ratings
const infraStars = document.querySelectorAll('input[name="infrastructure_rating"]');
const infraRatingValue = document.getElementById('infrastructure-rating-value');

infraStars.forEach(star => {
    star.addEventListener('change', () => {
        infraRatingValue.textContent = star.value;
    });
});


function showMore() {
    const hiddenReviews = document.querySelectorAll('.review-item.hidden');
    hiddenReviews.forEach(review => review.classList.remove('hidden'));
    
    // Hide the "Show More" button once all reviews are shown
    document.getElementById('show-more-button').style.display = 'none';
}
