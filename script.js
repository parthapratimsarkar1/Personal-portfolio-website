document.addEventListener("DOMContentLoaded", function() {
    const imageUpload = document.getElementById("image-upload");
    const profilePhoto = document.getElementById("profile-photo");

    // Set default image source
    profilePhoto.src = "profile-photo.png"; // Ensure this image is in the project directory

    // Listen for image upload
    imageUpload.addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profilePhoto.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
