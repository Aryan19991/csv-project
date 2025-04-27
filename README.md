i have the exam and the base code and questions and every task is given in this pdf give me the answer code completing all the requirements provided. Please, each and every requirement should be met.
Scenario1--------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .main-container {
            background-color: #f0e6e6;
            border-radius: 8px;
            width: 100%;
            max-width: 800px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }

        .student-info {
            background-color: #fff;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }

        .student-details {
            margin-bottom: 10px;
        }

        .form-section {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .avatar-selection {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 10px;
        }

        .avatar {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .avatar.selected {
            width: 80px;
            height: 80px;
            border: 3px solid #4CAF50;
        }

        .form-note {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }

        .submit-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            display: block;
            margin: 20px auto;
            font-size: 16px;
        }

        .submit-btn:hover {
            background-color: #45a049;
        }

        .profile-card {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            width: 80%;
            max-width: 400px;
            margin: 20px auto;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            display: block;
        }

        .profile-avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto 15px;
        }

        .error-message {
            color: #ff0000;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        .success-message {
            color: #4CAF50;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        .alert-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            display: none;
        }

        .alert-content {
            text-align: center;
        }

        .alert-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>Create Your Profile</h1>
        
        <div class="student-info">
            <div class="student-details">
                <strong>Student Full Name</strong>
                <div>Student ID - w123456</div>
                <div>The course you study</div>
            </div>
            <h3>User Details</h3>
        </div>
        
        <div class="form-section">
            <form id="profileForm">
                <div class="form-group">
                    <label for="username">Enter Your User Name:</label>
                    <input type="text" id="username" name="username">
                    <div id="usernameError" class="error-message"></div>
                    <div id="usernameSuccess" class="success-message">✓ Valid Username</div>
                    <div class="form-note">A valid username should contain 7 characters, starting with "w"</div>
                </div>
                
                <div class="form-group">
                    <label for="age">Enter Your Age:</label>
                    <input type="text" id="age" name="age" value="Between 19-25" readonly>
                    <div class="form-note">Do not change the user age</div>
                </div>
                
                <div class="form-group">
                    <label>Select an Avatar:</label>
                    <div class="avatar-selection">
                        <img src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" class="avatar" data-avatar="1" alt="Avatar 1">
                        <img src="https://via.placeholder.com/150/F15BB5/FFFFFF?text=2" class="avatar" data-avatar="2" alt="Avatar 2">
                        <img src="https://via.placeholder.com/150/FEE440/000000?text=3" class="avatar" data-avatar="3" alt="Avatar 3">
                    </div>
                    <input type="hidden" id="selectedAvatar" name="selectedAvatar" value="1">
                </div>
                
                <button type="submit" class="submit-btn" id="submitProfile">Submit Profile</button>
            </form>
        </div>
        
        <div class="profile-card" id="profileCard">
            <img id="profileAvatar" class="profile-avatar" src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" alt="Selected Avatar">
            <h2 id="profileName">[Your Name]</h2>
            <p>Age: <span id="profileAge">Between 19-25</span></p>
        </div>
    </div>
    
    <div class="alert-popup" id="alertPopup">
        <div class="alert-content">
            <p>Please fill all required fields before submitting.</p>
            <button class="alert-btn" id="alertOkBtn">OK</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const usernameInput = document.getElementById('username');
            const usernameError = document.getElementById('usernameError');
            const usernameSuccess = document.getElementById('usernameSuccess');
            const avatars = document.querySelectorAll('.avatar');
            const selectedAvatarInput = document.getElementById('selectedAvatar');
            const profileForm = document.getElementById('profileForm');
            const profileCard = document.getElementById('profileCard');
            const profileName = document.getElementById('profileName');
            const profileAge = document.getElementById('profileAge');
            const profileAvatar = document.getElementById('profileAvatar');
            const alertPopup = document.getElementById('alertPopup');
            const alertOkBtn = document.getElementById('alertOkBtn');
            
            // Initialize with first avatar selected
            avatars[0].classList.add('selected');
            
            // Username validation - only validate, don't update profile card
            usernameInput.addEventListener('input', function() {
                const value = this.value;
                
                // Clear previous messages
                usernameError.style.display = 'none';
                usernameSuccess.style.display = 'none';
                
                if (value.length === 0) {
                    // Empty input, do nothing
                    return;
                }
                
                if (value.length !== 7) {
                    usernameError.textContent = 'Username must be 7 characters long, starting with "w"';
                    usernameError.style.display = 'block';
                    return;
                }
                
                if (!value.startsWith('w')) {
                    usernameError.textContent = 'Username must start with "w"';
                    usernameError.style.display = 'block';
                    return;
                }
                
                // Valid username
                usernameSuccess.style.display = 'block';
            });
            
            // Avatar selection - only update the selection, don't update profile card
            avatars.forEach(avatar => {
                avatar.addEventListener('click', function() {
                    // Remove selected class from all avatars
                    avatars.forEach(a => a.classList.remove('selected'));
                    
                    // Add selected class to clicked avatar
                    this.classList.add('selected');
                    
                    // Store selected avatar value
                    const avatarValue = this.getAttribute('data-avatar');
                    selectedAvatarInput.value = avatarValue;
                });
            });
            
            // Form submission
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const username = usernameInput.value;
                const age = document.getElementById('age').value;
                const avatar = selectedAvatarInput.value;
                
                // Validate form
                if (!username || !username.startsWith('w') || username.length !== 7 || !avatar) {
                    alertPopup.style.display = 'block';
                    return;
                }
                
                // Update profile card only after successful submission
                profileName.textContent = username;
                profileAge.textContent = age;
                
                // Get the selected avatar image source
                const selectedAvatarImg = document.querySelector('.avatar.selected');
                if (selectedAvatarImg) {
                    profileAvatar.src = selectedAvatarImg.src;
                }
                
                // Show success alert
                alert('Profile submitted successfully!');
            });
            
            // Close alert popup
            alertOkBtn.addEventListener('click', function() {
                alertPopup.style.display = 'none';
            });
        });
    </script>
</body>
</html>

Scenario2-----------------------------------------------------------------------------
--------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .main-container {
            background-color: #f0e6e6;
            border-radius: 8px;
            width: 100%;
            max-width: 800px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }

        .student-info {
            background-color: #fff;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }

        .student-details {
            margin-bottom: 10px;
        }

        .form-section {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .avatar-selection {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 10px;
        }

        .avatar {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .avatar.selected {
            width: 80px;
            height: 80px;
            border: 3px solid #4CAF50;
        }

        .form-note {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }

        .submit-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            display: block;
            margin: 20px auto;
            font-size: 16px;
        }

        .submit-btn:hover {
            background-color: #45a049;
        }

        .profile-card {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            width: 80%;
            max-width: 400px;
            margin: 20px auto;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            display: block;
        }

        .profile-avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto 15px;
        }

        .error-message {
            color: #ff0000;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        .success-message {
            color: #4CAF50;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        .alert-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            display: none;
        }

        .alert-content {
            text-align: center;
        }

        .alert-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>Create Your Profile</h1>
        
        <div class="student-info">
            <div class="student-details">
                <strong>Student Full Name</strong>
                <div>Student ID - w123456</div>
                <div>The course you study</div>
            </div>
            <h3>User Details</h3>
        </div>
        
        <div class="form-section">
            <form id="profileForm">
                <div class="form-group">
                    <label for="username">Enter Your User Name:</label>
                    <input type="text" id="username" name="username" placeholder="7 characters no numbers">
                    <div id="usernameError" class="error-message"></div>
                    <div id="usernameSuccess" class="success-message">✓ Valid Username</div>
                    <div class="form-note">A valid username should contain 7 characters, no numbers</div>
                </div>
                
                <div class="form-group">
                    <label for="age">Enter Your Age:</label>
                    <input type="text" id="age" name="age" value="Between 19-25" readonly>
                    <div class="form-note">Do not change the user age</div>
                </div>
                
                <div class="form-group">
                    <label>Select an Avatar:</label>
                    <div class="avatar-selection">
                        <img src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" class="avatar selected" data-avatar="1" alt="Avatar 1">
                        <img src="https://via.placeholder.com/150/F15BB5/FFFFFF?text=2" class="avatar" data-avatar="2" alt="Avatar 2">
                        <img src="https://via.placeholder.com/150/FEE440/000000?text=3" class="avatar" data-avatar="3" alt="Avatar 3">
                    </div>
                    <input type="hidden" id="selectedAvatar" name="selectedAvatar" value="1">
                </div>
                
                <button type="submit" class="submit-btn" id="submitProfile">Submit Profile</button>
            </form>
        </div>
        
        <div class="profile-card" id="profileCard">
            <img id="profileAvatar" class="profile-avatar" src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" alt="Selected Avatar">
            <h2 id="profileName">[Your Name]</h2>
            <p>Age: <span id="profileAge">[Your Age]</span></p>
        </div>
    </div>
    
    <div class="alert-popup" id="alertPopup">
        <div class="alert-content">
            <p>Please fill all required fields before submitting.</p>
            <button class="alert-btn" id="alertOkBtn">OK</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const usernameInput = document.getElementById('username');
            const usernameError = document.getElementById('usernameError');
            const usernameSuccess = document.getElementById('usernameSuccess');
            const avatars = document.querySelectorAll('.avatar');
            const selectedAvatarInput = document.getElementById('selectedAvatar');
            const profileForm = document.getElementById('profileForm');
            const profileCard = document.getElementById('profileCard');
            const profileName = document.getElementById('profileName');
            const profileAge = document.getElementById('profileAge');
            const profileAvatar = document.getElementById('profileAvatar');
            const alertPopup = document.getElementById('alertPopup');
            const alertOkBtn = document.getElementById('alertOkBtn');
            
            // Username validation
            usernameInput.addEventListener('input', function() {
                const value = this.value;
                
                // Clear previous messages
                usernameError.style.display = 'none';
                usernameSuccess.style.display = 'none';
                
                if (value.length === 0) {
                    // Empty input, do nothing
                    return;
                }
                
                if (value.length !== 7) {
                    usernameError.textContent = 'You have not entered a seven character string';
                    usernameError.style.display = 'block';
                    return;
                }
                
                // Check if username contains numbers
                if (/\d/.test(value)) {
                    usernameError.textContent = 'Username must contain only letters';
                    usernameError.style.display = 'block';
                    return;
                }
                
                // Valid username
                usernameSuccess.style.display = 'block';
            });
            
            // Avatar selection
            avatars.forEach(avatar => {
                avatar.addEventListener('click', function() {
                    // Remove selected class from all avatars
                    avatars.forEach(a => a.classList.remove('selected'));
                    
                    // Add selected class to clicked avatar
                    this.classList.add('selected');
                    
                    // Store selected avatar value
                    const avatarValue = this.getAttribute('data-avatar');
                    selectedAvatarInput.value = avatarValue;
                });
            });
            
            // Form submission
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const username = usernameInput.value;
                const age = document.getElementById('age').value;
                const avatar = selectedAvatarInput.value;
                
                // Validate form
                if (!username || username.length !== 7 || /\d/.test(username) || !avatar) {
                    alertPopup.style.display = 'block';
                    return;
                }
                
                // Update profile card only after successful form submission
                profileName.textContent = username;
                profileAge.textContent = age;
                
                // Update avatar based on selection
                const selectedAvatarSrc = document.querySelector(`.avatar[data-avatar="${avatar}"]`).src;
                profileAvatar.src = selectedAvatarSrc;
            });
            
            // Close alert popup
            alertOkBtn.addEventListener('click', function() {
                alertPopup.style.display = 'none';
            });
        });
    </script>
</body>
</html>

Scenario3-----------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .main-container {
            background-color: #f0e6e6;
            border-radius: 8px;
            width: 100%;
            max-width: 800px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }

        .student-info {
            background-color: #fff;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }

        .student-details {
            margin-bottom: 10px;
        }

        .form-section {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        .avatar-selection {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 10px;
        }

        .avatar {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .avatar.selected {
            width: 80px;
            height: 80px;
            border: 3px solid #4CAF50;
        }

        .form-note {
            font-size: 12px;
            color: #666;
            margin-top: 5px;
        }

        .submit-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            display: block;
            margin: 20px auto;
            font-size: 16px;
        }

        .submit-btn:hover {
            background-color: #45a049;
        }

        .profile-card {
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            width: 80%;
            max-width: 400px;
            margin: 20px auto;
            text-align: center;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            border: 2px solid #f0e6e6;
            display: block;
        }

        .profile-avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto 15px;
        }

        .error-message {
            color: #ff0000;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        .success-message {
            color: #4CAF50;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }

        .alert-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            display: none;
        }

        .alert-content {
            text-align: center;
        }

        .alert-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 15px;
        }

        /* Study level dropdown styles */
        .study-level-dropdown {
            position: relative;
            display: inline-block;
            width: 100%;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            width: 100%;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
            border-radius: 4px;
            margin-top: 2px;
        }

        .dropdown-item {
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            color: black;
            cursor: pointer;
        }

        .dropdown-item:hover {
            background-color: #f1f1f1;
        }

        .dropdown-item.selected {
            background-color: #e7f3ff;
            color: #0066cc;
        }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>Create Your Profile</h1>
        
        <div class="student-info">
            <div class="student-details">
                <strong>Student Full Name</strong>
                <div>Student ID - w123456</div>
                <div>The course you study</div>
            </div>
            <h3>User Details</h3>
        </div>
        
        <div class="form-section">
            <form id="profileForm">
                <div class="form-group">
                    <label for="username">Your UserName is:</label>
                    <input type="text" id="username" name="username" value="w123456" readonly>
                    <div class="form-note">No need to change the User Name</div>
                </div>
                
                <div class="form-group">
                    <label for="age">Enter Your Age:</label>
                    <input type="number" id="age" name="age" min="18" placeholder="Min value 18">
                    <div id="ageError" class="error-message">Age must be between 18 and 70!</div>
                    <div id="ageSuccess" class="success-message">✓ Valid Age</div>
                    <div class="form-note">The minimum expected age is 18, else print feedback as below</div>
                </div>
                
                <div class="form-group">
                    <label for="studyLevel">Select the level of your studies:</label>
                    <select id="studyLevel" name="studyLevel">
                        <option value="Foundation">Foundation</option>
                        <option value="Undergraduate" selected>Undergraduate</option>
                        <option value="Postgraduate">Postgraduate</option>
                    </select>
                    <div class="form-note">Users can select their level of study. Undergraduate is pre-selected.</div>
                </div>
                
                <div class="form-group">
                    <label>Select an Avatar:</label>
                    <div class="avatar-selection">
                        <img src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" class="avatar" data-avatar="1" alt="Avatar 1">
                        <img src="https://via.placeholder.com/150/F15BB5/FFFFFF?text=2" class="avatar" data-avatar="2" alt="Avatar 2">
                        <img src="https://via.placeholder.com/150/FEE440/000000?text=3" class="avatar" data-avatar="3" alt="Avatar 3">
                    </div>
                    <input type="hidden" id="selectedAvatar" name="selectedAvatar">
                </div>
                
                <button type="submit" class="submit-btn" id="submitProfile">Submit Profile</button>
            </form>
        </div>
        
        <div class="profile-card" id="profileCard">
            <img id="profileAvatar" class="profile-avatar" src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" alt="Default Avatar">
            <h2 id="profileName">[Your UserName]</h2>
            <p>Age: <span id="profileAge">[Your Age]</span></p>
            <p>Study: <span id="profileStudy">[Your Study]</span></p>
        </div>
    </div>
    
    <div class="alert-popup" id="alertPopup">
        <div class="alert-content">
            <p>Please fill all required fields before submitting.</p>
            <button class="alert-btn" id="alertOkBtn">OK</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const usernameInput = document.getElementById('username');
            const ageInput = document.getElementById('age');
            const ageError = document.getElementById('ageError');
            const ageSuccess = document.getElementById('ageSuccess');
            const studyLevelSelect = document.getElementById('studyLevel');
            const avatars = document.querySelectorAll('.avatar');
            const selectedAvatarInput = document.getElementById('selectedAvatar');
            const profileForm = document.getElementById('profileForm');
            const profileCard = document.getElementById('profileCard');
            const profileName = document.getElementById('profileName');
            const profileAge = document.getElementById('profileAge');
            const profileStudy = document.getElementById('profileStudy');
            const profileAvatar = document.getElementById('profileAvatar');
            const alertPopup = document.getElementById('alertPopup');
            const alertOkBtn = document.getElementById('alertOkBtn');
            
            // Initialize with default values
            selectedAvatarInput.value = "1"; // Default to first avatar
            
            // Age validation - only show validation messages, don't update profile
            ageInput.addEventListener('input', function() {
                const ageValue = parseInt(this.value, 10);
                
                // Hide both messages initially
                ageError.style.display = 'none';
                ageSuccess.style.display = 'none';
                
                if (!this.value) {
                    // Empty input, do nothing
                    return;
                }
                
                if (isNaN(ageValue) || ageValue < 18 || ageValue > 70) {
                    ageError.style.display = 'block';
                    return;
                }
                
                // Valid age
                ageSuccess.style.display = 'block';
                
                // Removed real-time update of profile age
            });
            
            // Removed real-time update for study level
            
            // Avatar selection - only mark the avatar as selected without updating profile
            avatars.forEach(avatar => {
                avatar.addEventListener('click', function() {
                    // Remove selected class from all avatars
                    avatars.forEach(a => a.classList.remove('selected'));
                    
                    // Add selected class to clicked avatar
                    this.classList.add('selected');
                    
                    // Store selected avatar value
                    const avatarValue = this.getAttribute('data-avatar');
                    selectedAvatarInput.value = avatarValue;
                    
                    // Removed real-time update of profile avatar
                });
            });
            
            // Form submission - update profile only when submitted
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const age = ageInput.value;
                const studyLevel = studyLevelSelect.value;
                const avatar = selectedAvatarInput.value;
                
                // Validate form
                if (!age || isNaN(parseInt(age, 10)) || parseInt(age, 10) < 18 || parseInt(age, 10) > 70 || !avatar) {
                    alertPopup.style.display = 'block';
                    return;
                }
                
                // Update profile card with final values ONLY after valid submission
                profileName.textContent = usernameInput.value;
                profileAge.textContent = age;
                profileStudy.textContent = studyLevel;
                
                // Update avatar
                const selectedAvatarElement = document.querySelector(`.avatar[data-avatar="${avatar}"]`);
                if (selectedAvatarElement) {
                    profileAvatar.src = selectedAvatarElement.src;
                }
            });
            
            // Close alert popup
            alertOkBtn.addEventListener('click', function() {
                alertPopup.style.display = 'none';
            });
            
            // Make the first avatar selected by default
            avatars[0].classList.add('selected');
        });
    </script>
</body>
</html>

Scenario4----------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 800px;
            margin: 30px auto;
        }

        .profile-container {
            background-color: #a8d1e7; /* Light blue background */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #7a5e00;
            margin-bottom: 30px;
        }

        .form-section {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .student-info {
            text-align: center;
            margin-bottom: 20px;
        }

        .student-info p {
            margin: 5px 0;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .eligibility-feedback {
            color: #4caf50; /* Green for eligible */
            font-size: 12px;
            margin-top: 5px;
            display: block;
        }

        .ineligible {
            color: #ff0000; /* Red for ineligible */
        }

        .membership-options {
            margin-top: 15px;
        }

        .radio-group {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .radio-group input {
            width: auto;
            margin-right: 10px;
        }

        .discount-text {
            margin-left: 5px;
            color: #4caf50;
        }

        .submit-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            width: 100%;
            margin-top: 20px;
        }

        .submit-btn:hover {
            background-color: #45a049;
        }

        /* Profile Card Styles */
        .profile-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            margin-top: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            /* Display initially */
            display: block;
        }

        .profile-card h2 {
            color: #7a5e00;
            margin-bottom: 15px;
        }

        .profile-card p {
            margin: 5px 0;
        }

        .profile-image {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            overflow: hidden;
            margin: 0 auto 15px;
            background-color: #f1f1f1;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .profile-image img {
            width: 100%;
            height: auto;
        }

        /* Customization Section */
        .customization-section {
            margin-top: 30px;
        }

        .customization-section h2 {
            text-align: center;
            color: #7a5e00;
            margin-bottom: 15px;
        }

        .pattern-options {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }

        .pattern-option {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
        }

        .pattern-option.selected {
            border: 2px solid #4CAF50;
        }

        .pattern-option:nth-child(1) {
            background-color: #ffffff;
        }

        .pattern-option:nth-child(2) {
            background-color: #f1f1f1;
            background-image: radial-gradient(#ddd 2px, transparent 2px);
            background-size: 10px 10px;
        }

        .pattern-option:nth-child(3) {
            background-color: #f1f1f1;
            background-image: linear-gradient(45deg, #ddd 25%, transparent 25%, transparent 75%, #ddd 75%, #ddd),
                              linear-gradient(45deg, #ddd 25%, transparent 25%, transparent 75%, #ddd 75%, #ddd);
            background-size: 10px 10px;
            background-position: 0 0, 5px 5px;
        }

        /* Modal/Popup styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            align-items: center;
            justify-content: center;
        }

        .modal-content {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 8px;
            width: 80%;
            max-width: 400px;
            position: relative;
            text-align: center;
        }

        .modal-title {
            font-weight: bold;
            margin-bottom: 15px;
        }

        .modal-text {
            margin-bottom: 20px;
        }

        .ok-btn {
            background-color: #8B4513; /* Brown button color to match image */
            color: white;
            border: none;
            padding: 8px 25px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }

        .ok-btn:hover {
            background-color: #A0522D;
        }

        /* Section dividers */
        .section-divider {
            border-top: 1px solid #8bb5c9;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="profile-container" id="profileContainer">
            <h1>Create Your Profile</h1>
            
            <!-- Student Information Section -->
            <div class="student-info">
                <p><strong>Student Full Name</strong></p>
                <p><strong>Student ID:</strong> w123457</p>
                <p><strong>The course you study</strong></p>
            </div>
            
            <!-- User Details Section - This will be the one with pattern applied -->
            <div class="form-section" id="userDetailsSection">
                <h2>User Details</h2>
                <form id="profileForm">
                    <div class="form-group">
                        <label for="userName">User Name:</label>
                        <input type="text" id="userName" value="Oliver Brown" readonly>
                    </div>
                    
                    <div class="form-group">
                        <label for="age">Age:</label>
                        <input type="number" id="age" placeholder="Enter an age above 18" value="21">
                        <p class="eligibility-feedback" id="ageEligibility">✓ You are eligible for discount</p>
                    </div>
                    
                    <div class="form-group">
                        <label for="studyStatus">Study status:</label>
                        <select id="studyStatus">
                            <option value="FT UG student" selected>FT UG student</option>
                            <option value="PT UG student">PT UG student</option>
                            <option value="PG student">PG student</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="subscription">Subscription:</label>
                        <select id="subscription">
                            <option value="Standard £9.99 per/month" selected>Standard £9.99 per/month</option>
                            <option value="Premium £19.99 per/month">Premium £19.99 per/month</option>
                            <option value="Basic £4.99 per/month">Basic £4.99 per/month</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>Annual membership discount:</label>
                        <div class="membership-options">
                            <div class="radio-group">
                                <input type="radio" id="annualMembership" name="membership" value="annual">
                                <label for="annualMembership">Annual membership apply</label>
                                <span class="discount-text">20% Discount</span>
                            </div>
                            
                            <div class="radio-group">
                                <input type="radio" id="noDiscount" name="membership" value="none" checked>
                                <label for="noDiscount">Without Discount</label>
                            </div>
                        </div>
                    </div>
                    
                    <button type="submit" class="submit-btn" id="submitProfile">Submit Profile</button>
                </form>
            </div>
            
            <!-- Profile Card (Initially showing placeholder values) -->
            <div class="profile-card" id="profileCard">
                <h2>Your Profile</h2>
                <div class="profile-image">
                    <img src="https://picsum.photos/200" alt="Profile Image" id="profileImage">
                </div>
                <p><strong id="cardName">[Your Name]</strong></p>
                <p>Study: <span id="cardStudy">[Study Status]</span></p>
                <p>Subscription: <span id="cardSubscription">[Your Subscription Choice]</span></p>
            </div>
            
            <div class="section-divider"></div>
            
            <!-- Customization Section -->
            <div class="customization-section">
                <h2>Customization</h2>
                <p style="text-align: center; margin-bottom: 10px;">Change the Background Pattern</p>
                <div class="pattern-options">
                    <div class="pattern-option selected" data-pattern="solid"></div>
                    <div class="pattern-option" data-pattern="dots"></div>
                    <div class="pattern-option" data-pattern="grid"></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Subscription Change Popup Modal -->
    <div class="modal" id="subscriptionModal">
        <div class="modal-content">
            <div class="modal-title">This page says</div>
            <div class="modal-text">Your subscription choice changed, press submit profile to re-calculate your discount.</div>
            <button class="ok-btn" id="okButton">OK</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Elements
            const ageInput = document.getElementById('age');
            const ageEligibility = document.getElementById('ageEligibility');
            const profileForm = document.getElementById('profileForm');
            const profileCard = document.getElementById('profileCard');
            const cardName = document.getElementById('cardName');
            const cardStudy = document.getElementById('cardStudy');
            const cardSubscription = document.getElementById('cardSubscription');
            const studyStatus = document.getElementById('studyStatus');
            const subscription = document.getElementById('subscription');
            const annualMembership = document.getElementById('annualMembership');
            const userDetailsSection = document.getElementById('userDetailsSection');
            const patternOptions = document.querySelectorAll('.pattern-option');
            const subscriptionModal = document.getElementById('subscriptionModal');
            const okButton = document.getElementById('okButton');
            
            // Track last subscription value to detect changes
            let lastSubscription = subscription.value;
            
            // Check age eligibility for discount (run immediately on page load)
            function checkAgeEligibility() {
                const age = parseInt(ageInput.value);
                if (age >= 18) {
                    ageEligibility.textContent = "✓ You are eligible for discount";
                    ageEligibility.classList.remove('ineligible');
                } else {
                    ageEligibility.textContent = "✗ You are not eligible for discount";
                    ageEligibility.classList.add('ineligible');
                }
            }
            
            // Run immediately to show initial status
            checkAgeEligibility();
            
            // Update when age changes - but only update the eligibility text, not the profile card
            ageInput.addEventListener('input', checkAgeEligibility);
            
            // Show popup when subscription changes
            subscription.addEventListener('change', function() {
                if (this.value !== lastSubscription) {
                    subscriptionModal.style.display = 'flex';
                    lastSubscription = this.value;
                }
            });
            
            // Close modal when OK button is clicked
            okButton.addEventListener('click', function() {
                subscriptionModal.style.display = 'none';
            });
            
            // Handle form submission - ONLY update profile card here
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Update the profile card with form values ONLY after submission
                cardName.textContent = document.getElementById('userName').value;
                cardStudy.textContent = studyStatus.value;
                
                // Format subscription text for the profile card
                let subscriptionText = subscription.value;
                
                // Extract just the plan type and price
                const planMatch = subscriptionText.match(/(Standard|Premium|Basic) £(\d+\.\d+)/);
                if (planMatch) {
                    const planType = planMatch[1];
                    const price = planMatch[2];
                    
                    // Apply discount if annual membership is selected
                    if (annualMembership.checked) {
                        const discountedPrice = (parseFloat(price) * 0.8).toFixed(2); // 20% discount
                        subscriptionText = `${planType} £${discountedPrice} per/month (after 20% discount)`;
                    } else {
                        subscriptionText = `${planType} £${price} per/month`;
                    }
                }
                
                cardSubscription.textContent = subscriptionText;
                
                // Scroll to see the profile card
                setTimeout(() => {
                    profileCard.scrollIntoView({ behavior: 'smooth' });
                }, 300);
            });
            
            // Initialize profile card with PLACEHOLDER values instead of real data
            // This keeps the placeholders until the form is submitted
            
            // Handle pattern selection
            patternOptions.forEach(option => {
                option.addEventListener('click', function() {
                    // Remove selected class from all options
                    patternOptions.forEach(opt => opt.classList.remove('selected'));
                    
                    // Add selected class to the clicked option
                    this.classList.add('selected');
                    
                    // Apply pattern ONLY to the user details section
                    const pattern = this.getAttribute('data-pattern');
                    applyPattern(pattern);
                });
            });
            
            // Function to apply background pattern to user details section only
            function applyPattern(pattern) {
                // Reset all patterns
                userDetailsSection.style.backgroundImage = 'none';
                userDetailsSection.style.backgroundColor = '#fff';
                
                // Apply selected pattern
                switch(pattern) {
                    case 'dots':
                        userDetailsSection.style.backgroundImage = 'radial-gradient(#ddd 2px, transparent 2px)';
                        userDetailsSection.style.backgroundSize = '20px 20px';
                        break;
                    case 'grid':
                        userDetailsSection.style.backgroundImage = 'linear-gradient(#ddd 1px, transparent 1px), linear-gradient(90deg, #ddd 1px, transparent 1px)';
                        userDetailsSection.style.backgroundSize = '20px 20px';
                        break;
                    default:
                        // Solid pattern (default)
                        break;
                }
            }
        });
    </script>
</body>
</html>

Scenario5----------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 600px;
            margin: 30px auto;
        }

        .profile-container {
            background-color: #e8e0e0;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
        }

        h2 {
            text-align: center;
            border-bottom: 1px solid #ccc;
            padding-bottom: 10px;
            margin-bottom: 15px;
            font-size: 18px;
        }

        .student-info {
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
        }

        .student-info p {
            margin: 5px 0;
            font-size: 14px;
        }

        .form-section {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }

        .form-group label {
            width: 100px;
            margin-right: 10px;
            font-weight: normal;
        }

        .form-group input,
        .form-group select {
            flex: 1;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        /* Human Verification Styles */
        .verification {
            text-align: center;
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .verification h2 {
            margin-bottom: 15px;
        }

        .verify-btn {
            background-color: #f0f0f0;
            color: #333;
            border: 1px solid #ccc;
            padding: 5px 15px;
            border-radius: 4px;
            cursor: pointer;
        }

        .verify-btn:hover {
            background-color: #e0e0e0;
        }

        .submit-btn {
            background-color: #69b578;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            width: 100%;
            margin-top: 20px;
            display: none; /* Hidden initially */
        }

        .submit-btn:hover {
            background-color: #539e62;
        }

        /* Profile Card Styles */
        .profile-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: none; /* Hidden initially */
        }

        .profile-details {
            display: flex;
            align-items: center;
        }

        .profile-image {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background-color: #f1dc5a;
            margin-right: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #333;
            font-weight: bold;
        }

        .profile-info {
            flex: 1;
        }

        .profile-info h3 {
            margin-bottom: 5px;
            color: #333;
        }

        .profile-info p {
            margin: 5px 0;
            color: #555;
        }

        /* Customization Section */
        .customization-section {
            margin-top: 20px;
        }

        .pattern-options {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }

        .pattern-option {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
            background-color: white;
        }

        .pattern-option.selected {
            border: 2px solid #69b578;
        }
        
        .profile-caption {
            background-color: #f0f0f0;
            padding: 10px;
            text-align: center;
            color: #228B22;
            font-style: italic;
            margin-top: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="profile-container" id="profileContainer">
            <h1>Create Your Profile</h1>
            
            <!-- Student Information Section -->
            <div class="student-info">
                <p>Student Full Name</p>
                <p>Student ID - w1234567</p>
                <p>The course you study</p>
            </div>
            
            <!-- Form Section -->
            <h2>User Details</h2>
            <div class="form-section">
                <form id="profileForm">
                    <div class="form-group">
                        <label for="userName">User Name:</label>
                        <input type="text" id="userName" value="Tom Boyle" readonly>
                    </div>
                    
                    <div class="form-group">
                        <label for="studyStatus">Study status:</label>
                        <input type="text" id="studyStatus" value="FT UG student" readonly>
                    </div>
                    
                    <div class="form-group">
                        <label for="tuitionFees">Tuition fees:</label>
                        <select id="tuitionFees">
                            <option value="UK tuition fee £9,535">UK tuition fee £9,535</option>
                            <option value="International tuition fee £17,000">International tuition fee £17,000</option>
                            <option value="Full tution fee waiver">Full tution fee waiver</option>
                        </select>
                    </div>
                </form>
            </div>
            
            <!-- Human Verification Section -->
            <h2>Verify you are human</h2>
            <div class="verification">
                <button type="button" id="verifyBtn" class="verify-btn">Click to Verify</button>
            </div>
            
            <!-- Submit Button (Initially Hidden) -->
            <button type="submit" id="submitProfile" class="submit-btn">Submit Profile</button>
            
            <!-- Profile Card (Hidden initially) -->
            <div class="profile-card" id="profileCard">
                <h2>Your Profile</h2>
                <div class="profile-details">
                    <div class="profile-image" id="profileImage">
                        <span>👤</span>
                    </div>
                    <div class="profile-info">
                        <h3 id="cardName">[Your Name]</h3>
                        <p>Study: <span id="cardStudy">[Study Status]</span></p>
                        <p>Tuition Fees: <span id="cardTuitionFees">[Your Tuition Fees]</span></p>
                    </div>
                </div>
                <div class="profile-caption">
                    The user profile details after submitting the user profile
                </div>
            </div>
            
            <!-- Customization Section -->
            <h2>Customization</h2>
            <div class="customization-section">
                <p style="text-align: center; margin-bottom: 10px;">Change the Background Pattern</p>
                <div class="pattern-options">
                    <div class="pattern-option selected" data-pattern="solid"></div>
                    <div class="pattern-option" data-pattern="dots"></div>
                    <div class="pattern-option" data-pattern="grid"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Elements
            const profileForm = document.getElementById('profileForm');
            const profileCard = document.getElementById('profileCard');
            const cardName = document.getElementById('cardName');
            const cardStudy = document.getElementById('cardStudy');
            const cardTuitionFees = document.getElementById('cardTuitionFees');
            const userName = document.getElementById('userName');
            const studyStatus = document.getElementById('studyStatus');
            const tuitionFees = document.getElementById('tuitionFees');
            const profileContainer = document.getElementById('profileContainer');
            const patternOptions = document.querySelectorAll('.pattern-option');
            const verifyBtn = document.getElementById('verifyBtn');
            const submitBtn = document.getElementById('submitProfile');
            
            // Generate random math question for CAPTCHA
            function generateMathQuestion() {
                const num1 = Math.floor(Math.random() * 10) + 2; // Random number between 2-12
                const num2 = Math.floor(Math.random() * 10) + 2; // Random number between 2-12
                return {
                    num1: num1,
                    num2: num2,
                    answer: num1 * num2
                };
            }
            
            // Verify human check using alert with random math question
            verifyBtn.addEventListener('click', function() {
                // Generate random math question
                const mathQuestion = generateMathQuestion();
                
                // Show multiplication challenge in alert
                const userAnswer = prompt(`This page says\n\nWhat is ${mathQuestion.num1} * ${mathQuestion.num2}?`);
                
                if (userAnswer !== null) {
                    const userAnswerValue = parseInt(userAnswer);
                    
                    if (userAnswerValue === mathQuestion.answer) {
                        alert("This page says\n\nCorrect! You may now submit your profile.");
                        submitBtn.style.display = 'block'; // Show submit button after successful verification
                    } else {
                        alert("This page says\n\nIncorrect. Try again.");
                        submitBtn.style.display = 'none'; // Hide submit button if verification fails
                    }
                }
            });
            
            // Handle form submission
            submitBtn.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Update the profile card with actual values from form
                cardName.textContent = userName.value;
                cardStudy.textContent = studyStatus.value;
                cardTuitionFees.textContent = tuitionFees.value;
                
                // Show the profile card
                profileCard.style.display = 'block';
                
                // Scroll to see the profile card
                setTimeout(() => {
                    profileCard.scrollIntoView({ behavior: 'smooth' });
                }, 300);
            });
            
            // Handle pattern selection
            patternOptions.forEach(option => {
                option.addEventListener('click', function() {
                    // Remove selected class from all options
                    patternOptions.forEach(opt => opt.classList.remove('selected'));
                    
                    // Add selected class to the clicked option
                    this.classList.add('selected');
                    
                    // Apply pattern to the profile container
                    const pattern = this.getAttribute('data-pattern');
                    applyPattern(pattern);
                });
            });
            
            // Function to apply background pattern
            function applyPattern(pattern) {
                // Reset all patterns
                profileContainer.style.backgroundImage = 'none';
                profileContainer.style.backgroundColor = '#e8e0e0';
                
                // Apply selected pattern
                switch(pattern) {
                    case 'dots':
                        profileContainer.style.backgroundImage = 'radial-gradient(#ccc 2px, transparent 2px)';
                        profileContainer.style.backgroundSize = '20px 20px';
                        break;
                    case 'grid':
                        profileContainer.style.backgroundImage = 'linear-gradient(#ccc 1px, transparent 1px), linear-gradient(90deg, #ccc 1px, transparent 1px)';
                        profileContainer.style.backgroundSize = '20px 20px';
                        break;
                    default:
                        // Solid pattern (default)
                        break;
                }
            }
        });
    </script>
</body>
</html>

Scenario6------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            /* This will be modified by the pattern selection */
        }

        .container {
            width: 90%;
            max-width: 800px;
            margin: 30px auto;
        }

        .profile-header {
            background-color: #e0e0e0;
            padding: 15px;
            text-align: center;
            border-radius: 8px 8px 0 0;
            border-bottom: 1px solid #ccc;
        }

        .profile-header h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 5px;
        }

        .profile-header p {
            color: #555;
            font-size: 14px;
            margin: 3px 0;
        }

        .profile-container {
            background-color: #e8e0e0;
            padding: 20px;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 24px;
        }

        .student-info {
            text-align: center;
            margin-bottom: 20px;
            border: 2px solid #69b578;
            border-radius: 20px;
            padding: 10px;
            max-width: 400px;
            margin: 0 auto 20px;
        }

        .student-info p {
            margin: 5px 0;
            font-size: 14px;
        }

        .form-section {
            margin-bottom: 20px;
        }

        .form-section h2 {
            margin-bottom: 15px;
            color: #333;
            font-size: 18px;
            text-align: center;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input,
        .form-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        /* Human Verification Styles */
        .verification {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            text-align: center;
        }

        .verification h3 {
            margin-bottom: 10px;
            color: #333;
            text-align: center;
        }

        .verify-btn {
            background-color: #f0f0f0;
            color: black;
            border: 1px solid #ccc;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: normal;
            display: block;
            margin: 0 auto;
        }

        .verify-btn:hover {
            background-color: #e0e0e0;
        }

        .submit-btn {
            background-color: #f0f0f0;
            color: black;
            border: 1px solid #ccc;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: normal;
            display: block;
            margin: 20px auto 0;
            width: auto;
        }

        .submit-btn:hover {
            background-color: #e0e0e0;
        }

        /* Profile Card Styles */
        .profile-card {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px auto;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: none; /* Hidden initially */
            max-width: 400px;
        }

        .profile-card h2 {
            text-align: center;
            margin-bottom: 15px;
            font-size: 22px;
        }

        .divider {
            height: 1px;
            background-color: #ddd;
            margin: 10px 0 20px;
        }

        .profile-details {
            display: flex;
            align-items: flex-start;
        }

        .profile-image {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            overflow: hidden;
            margin-right: 20px;
            background-color: #9370DB;
            border: 3px solid #FFD700;
        }

        .profile-image img {
            width: 100%;
            height: auto;
        }

        .profile-info {
            flex: 1;
        }

        .profile-info h3 {
            margin-bottom: 15px;
            color: #333;
            font-size: 20px;
        }

        .profile-info p {
            margin: 5px 0;
            color: #333;
            font-size: 16px;
        }

        /* Dialog Styles */
        .dialog-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 100;
            display: none;
        }

        .dialog {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            width: 90%;
            max-width: 400px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .dialog p {
            margin-bottom: 20px;
        }

        .dialog-input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-bottom: 15px;
        }

        .dialog-buttons {
            display: flex;
            justify-content: flex-end;
        }

        .dialog-btn {
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-left: 10px;
            border: none;
            font-weight: bold;
        }

        .ok-btn {
            background-color: #b88456;
            color: white;
        }

        .cancel-btn {
            background-color: #eee;
            color: #333;
        }

        /* Customization Section */
        .customization-section {
            margin-top: 30px;
            border-top: 1px solid #ccc;
            padding-top: 20px;
        }

        .customization-section h2 {
            margin-bottom: 15px;
            color: #333;
            font-size: 18px;
            text-align: center;
        }

        .pattern-options {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }

        .pattern-option {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
        }

        .pattern-option.selected {
            border: 2px solid #FFD700;
        }

        .pattern-option:nth-child(1) {
            background-color: #e8e0e0;
        }

        .pattern-option:nth-child(2) {
            background-color: #f1f1f1;
            background-image: radial-gradient(#ddd 2px, transparent 2px);
            background-size: 10px 10px;
        }

        .pattern-option:nth-child(3) {
            background-color: #f1f1f1;
            background-image: linear-gradient(45deg, #ddd 25%, transparent 25%, transparent 75%, #ddd 75%, #ddd),
                              linear-gradient(45deg, #ddd 25%, transparent 25%, transparent 75%, #ddd 75%, #ddd);
            background-size: 10px 10px;
            background-position: 0 0, 5px 5px;
        }

        /* Hidden profile section */
        .hidden-profile-section {
            margin: 20px auto;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #f5f5f5;
            text-align: center;
            max-width: 400px;
            display: none; /* Initially hidden */
        }

        .hidden-profile-text {
            color: #28a745;
            font-style: italic;
            font-size: 16px;
        }

        .person-icon {
            border-radius: 50%;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 40px;
            background-color: #9370DB;
        }

        /* User details container */
        .user-details-container {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
        }

        .user-details-container h2 {
            text-align: center;
            margin-bottom: 15px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- New Profile Header -->
        <div class="profile-header">
            <h1>Create Your Profile</h1>
            <p>Student Full Name</p>
            <p>Student ID - w1234567</p>
            <p>The course you study</p>
        </div>

        <div class="profile-container" id="profileContainer">
            <!-- Form Section -->
            <div class="form-section">
                <div class="user-details-container">
                    <h2>User Details</h2>
                    <form id="profileForm">
                        <div class="form-group">
                            <label for="userName">User Name:</label>
                            <input type="text" id="userName" value="Sam Patel" readonly>
                        </div>
                        
                        <div class="form-group">
                            <label for="studyStatus">Study status:</label>
                            <input type="text" id="studyStatus" value="FT UG student" readonly>
                        </div>
                        
                        <div class="form-group">
                            <label for="subscription">Subscription:</label>
                            <select id="subscription">
                                <option value="Standard £9.99 per/month">Standard £9.99 per/month</option>
                                <option value="Premium £19.99 per/month" selected>Premium £19.99 per/month</option>
                                <option value="Basic £4.99 per/month">Basic £4.99 per/month</option>
                            </select>
                        </div>
                    </form>
                </div>
                
                <!-- Human Verification Section -->
                <div class="verification">
                    <h3>Verify you are human</h3>
                    <button type="button" id="verifyBtn" class="verify-btn">Click to Verify</button>
                </div>
                
                <button type="submit" id="submitProfile" class="submit-btn" style="display: none;">Submit Profile</button>
            </div>
            
            <!-- Hidden Profile Values Section -->
            <div class="hidden-profile-section" id="hiddenProfileSection">
                <p class="hidden-profile-text">The user profile details before submitting the user profile</p>
            </div>
            
            <!-- Profile Card -->
            <div class="profile-card" id="profileCard">
                <h2>Your Profile</h2>
                <div class="divider"></div>
                <div class="profile-details">
                    <div class="profile-image">
                        <div class="person-icon">👤</div>
                    </div>
                    <div class="profile-info">
                        <h3 id="cardName">Sam Patel</h3>
                        <p><strong>Study:</strong> <span id="cardStudy">FT UG student</span></p>
                        <p><strong>Subscription:</strong> <span id="cardSubscription">Premium £19.99 per/month</span></p>
                    </div>
                </div>
            </div>
            
            <!-- Customization Section -->
            <div class="customization-section">
                <h2>Customization</h2>
                <p style="text-align: center; margin-bottom: 15px;">Change the Background Pattern</p>
                <div class="pattern-options">
                    <div class="pattern-option selected" data-pattern="solid"></div>
                    <div class="pattern-option" data-pattern="dots"></div>
                    <div class="pattern-option" data-pattern="grid"></div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Math Verification Dialog -->
    <div class="dialog-overlay" id="mathDialog">
        <div class="dialog">
            <p>This page says</p>
            <p>What is <span id="num1">5</span> + <span id="num2">3</span> = ?</p>
            <input type="number" id="userAnswer" class="dialog-input" min="0">
            <div class="dialog-buttons">
                <button class="dialog-btn cancel-btn" id="cancelMathBtn">Cancel</button>
                <button class="dialog-btn ok-btn" id="okMathBtn">OK</button>
            </div>
        </div>
    </div>
    
    <!-- Success Dialog -->
    <div class="dialog-overlay" id="successDialog">
        <div class="dialog">
            <p>This page says</p>
            <p id="successText">Correct! You may now submit your profile.</p>
            <div class="dialog-buttons">
                <button class="dialog-btn ok-btn" id="okSuccessBtn">OK</button>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Elements
            const profileForm = document.getElementById('profileForm');
            const profileCard = document.getElementById('profileCard');
            const hiddenProfileSection = document.getElementById('hiddenProfileSection');
            const cardName = document.getElementById('cardName');
            const cardStudy = document.getElementById('cardStudy');
            const cardSubscription = document.getElementById('cardSubscription');
            const userName = document.getElementById('userName');
            const studyStatus = document.getElementById('studyStatus');
            const subscription = document.getElementById('subscription');
            const profileContainer = document.getElementById('profileContainer');
            const patternOptions = document.querySelectorAll('.pattern-option');
            const verifyBtn = document.getElementById('verifyBtn');
            const submitBtn = document.getElementById('submitProfile');
            const bodyElement = document.body; // Get the body element for background changes
            
            // Make sure the hidden profile section is initially hidden
            hiddenProfileSection.style.display = 'none';
            
            // Dialog elements
            const mathDialog = document.getElementById('mathDialog');
            const successDialog = document.getElementById('successDialog');
            const userAnswer = document.getElementById('userAnswer');
            const okMathBtn = document.getElementById('okMathBtn');
            const cancelMathBtn = document.getElementById('cancelMathBtn');
            const okSuccessBtn = document.getElementById('okSuccessBtn');
            const successText = document.getElementById('successText');
            
            // Generate random math challenge
            function generateMathChallenge() {
                let num1 = Math.floor(Math.random() * 10) + 1;
                let num2 = Math.floor(Math.random() * 10) + 1;
                document.getElementById('num1').textContent = num1;
                document.getElementById('num2').textContent = num2;
                return { num1, num2 };
            }
            
            // Generate initial math challenge
            let mathChallenge = generateMathChallenge();
            
            // Open verification dialog
            verifyBtn.addEventListener('click', function() {
                // Generate new math challenge each time
                mathChallenge = generateMathChallenge();
                mathDialog.style.display = 'flex';
                userAnswer.value = ''; // Clear previous answer
                userAnswer.focus();
            });
            
            // Handle math verification
            okMathBtn.addEventListener('click', function() {
                const correctAnswer = mathChallenge.num1 + mathChallenge.num2;
                const userAnswerValue = parseInt(userAnswer.value);
                
                mathDialog.style.display = 'none';
                
                if (userAnswerValue === correctAnswer) {
                    // Show success dialog
                    successDialog.style.display = 'flex';
                    successText.textContent = "Correct! You may now submit your profile.";
                    
                    // Enable submit button
                    submitBtn.style.display = 'block';
                } else {
                    // Show error dialog
                    successDialog.style.display = 'flex';
                    successText.textContent = "Incorrect. Try again.";
                }
            });
            
            // Cancel button in math dialog
            cancelMathBtn.addEventListener('click', function() {
                mathDialog.style.display = 'none';
            });
            
            // OK button in success dialog
            okSuccessBtn.addEventListener('click', function() {
                successDialog.style.display = 'none';
            });
            
            // Add event listener to submit button
            submitBtn.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Update the profile card with form values after a short delay
                setTimeout(() => {
                    cardName.textContent = userName.value;
                    cardStudy.textContent = studyStatus.value;
                    cardSubscription.textContent = subscription.value;
                    
                    // Hide the hidden profile section
                    hiddenProfileSection.style.display = 'none';
                    
                    // Show the profile card
                    profileCard.style.display = 'block';
                    
                    // Scroll to see the profile card
                    profileCard.scrollIntoView({ behavior: 'smooth' });
                }, 1500); // Show the "submitting" message for 1.5 seconds
            });
            
            // Handle pattern selection
            patternOptions.forEach(option => {
                option.addEventListener('click', function() {
                    // Remove selected class from all options
                    patternOptions.forEach(opt => opt.classList.remove('selected'));
                    
                    // Add selected class to the clicked option
                    this.classList.add('selected');
                    
                    // Apply pattern to the BODY element instead of profile container
                    const pattern = this.getAttribute('data-pattern');
                    applyPattern(pattern);
                });
            });
            
            // Function to apply background pattern to the BODY
            function applyPattern(pattern) {
                // Reset all patterns
                bodyElement.style.backgroundImage = 'none';
                bodyElement.style.backgroundColor = '#f5f5f5'; // Default background color
                
                // Apply selected pattern
                switch(pattern) {
                    case 'dots':
                        bodyElement.style.backgroundColor = '#f1f1f1';
                        bodyElement.style.backgroundImage = 'radial-gradient(#ccc 2px, transparent 2px)';
                        bodyElement.style.backgroundSize = '20px 20px';
                        break;
                    case 'grid':
                        bodyElement.style.backgroundColor = '#f1f1f1';
                        bodyElement.style.backgroundImage = 'linear-gradient(#ccc 1px, transparent 1px), linear-gradient(90deg, #ccc 1px, transparent 1px)';
                        bodyElement.style.backgroundSize = '20px 20px';
                        break;
                    default:
                        // Solid pattern (default)
                        bodyElement.style.backgroundColor = '#e8e0e0';
                        break;
                }
            }
            
            // Handle keypress in math dialog
            userAnswer.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    okMathBtn.click();
                }
            });
        });
    </script>
</body>
</html>

Scenario7---------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #e9e0df;
            display: flex;
            justify-content: center;
            padding: 20px;
            margin: 0;
        }
        
        .container {
            width: 100%;
            max-width: 800px;
            text-align: center;
        }
        
        .profile-card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .header {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        
        .student-info {
            text-align: left;
            margin-bottom: 15px;
            padding: 10px;
            background-color: #f8f8f8;
            border-radius: 5px;
        }
        
        .form-group {
            display: flex;
            margin-bottom: 15px;
            align-items: center;
        }
        
        .form-group label {
            width: 150px;
            text-align: left;
        }
        
        .form-control {
            flex: 1;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        
        .avatars {
            display: flex;
            justify-content: flex-start;
            margin-top: 10px;
            gap: 15px;
        }
        
        .avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            cursor: pointer;
            opacity: 0.7;
            transition: all 0.3s ease;
        }
        
        .avatar.selected {
            border: 3px solid #8bc34a;
            opacity: 1;
            transform: scale(1.1);
        }
        
        .btn-submit {
            background-color: #8bc34a;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 15px;
        }
        
        .alert-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        
        .alert-content {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            max-width: 400px;
            width: 100%;
            position: relative;
        }
        
        .alert-title {
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .alert-message {
            margin-bottom: 15px;
        }
        
        .alert-icon {
            color: #ff9800;
            margin-right: 5px;
        }
        
        .alert-btn {
            background-color: #8d6e63;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 20px;
            cursor: pointer;
        }
        
        .user-profile-card {
            display: none; /* Changed from block to none to hide initially */
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            border: 2px solid #ff9e80;
        }
        
        .profile-header {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 15px;
            text-align: center;
        }
        
        .profile-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            margin: 0 auto 15px;
            display: block;
            border: 2px solid #ccc;
        }
        
        .profile-detail {
            margin-bottom: 8px;
            text-align: right;
            margin-right: 30%;
        }

        .valid-age-indicator {
            color: green;
            font-size: 14px;
            margin-left: 10px;
            display: none;
        }
        
        .invalid-age-indicator {
            color: red;
            font-size: 14px;
            margin-left: 10px;
            display: none;
        }

        hr {
            border: 0;
            border-top: 1px solid #eee;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">Create Your Profile</div>
        
        <div class="profile-card">
            <div class="student-info">
                <div><strong>Student Full Name</strong></div>
                <div><strong>Student ID:</strong> w123456</div>
                <div><strong>The course you study</strong></div>
            </div>
            
            <div class="form-section">
                <div><strong>User Details</strong></div>
                
                <div class="form-group">
                    <label for="username">UserName:</label>
                    <input type="text" id="username" class="form-control" value="wminComp" readonly>
                </div>
                
                <div class="form-group">
                    <label for="age">Your Age:</label>
                    <input type="number" id="age" class="form-control" min="18" placeholder="Min value 18">
                    <span class="valid-age-indicator" id="validAgeIndicator">✓ Valid Age</span>
                    <span class="invalid-age-indicator" id="invalidAgeIndicator">✗ Age must be between 18 and 70!</span>
                </div>
                
                <div class="form-group">
                    <label for="level">The level you study:</label>
                    <select id="level" class="form-control">
                        <option value="Foundation" selected>Foundation</option>
                        <option value="Undergraduate">Undergraduate</option>
                        <option value="Postgraduate">Postgraduate</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Select an Avatar:</label>
                    <div class="avatars">
                        <img src="https://place-hold.it/60x60/ffe0b2/856404&text=1" class="avatar" data-avatar="1" alt="Avatar 1">
                        <img src="https://place-hold.it/60x60/bbdefb/0d47a1&text=2" class="avatar" data-avatar="2" alt="Avatar 2">
                        <img src="https://place-hold.it/60x60/e1bee7/6a1b9a&text=3" class="avatar" data-avatar="3" alt="Avatar 3">
                    </div>
                </div>
            </div>
            
            <button id="submitBtn" class="btn-submit">Submit Profile</button>
        </div>
        
        <!-- First Alert Modal -->
        <div class="alert-modal" id="generalAlert">
            <div class="alert-content">
                <div class="alert-title">This page says</div>
                <div class="alert-message">
                    <span class="alert-icon">⚠️</span>
                    <span>Please fill in all required fields before submitting.</span>
                </div>
                <button class="alert-btn" id="generalAlertOkBtn">OK</button>
            </div>
        </div>
        
        <!-- Second Alert Modal (Age-specific) -->
        <div class="alert-modal" id="ageAlert">
            <div class="alert-content">
                <div class="alert-title">This page says</div>
                <div class="alert-message">
                    <span class="alert-icon">⚠️</span>
                    <span>Age must be between 18 and 70!</span>
                </div>
                <button class="alert-btn" id="ageAlertOkBtn">OK</button>
            </div>
        </div>
        
        <!-- User Profile Card - Initially hidden and shown after validation -->
        <div class="user-profile-card" id="userProfileCard">
            <div class="profile-header">Your Profile</div>
            <hr>
            <img id="profileAvatar" src="https://place-hold.it/80x80/ffe0b2/856404&text=1" class="profile-avatar" alt="Profile Avatar">
            <div class="profile-detail"><strong>UserName:</strong> wminComp</div>
            <div class="profile-detail"><strong>Age:</strong> <span id="profileAge"></span></div>
            <div class="profile-detail"><strong>Study:</strong> <span id="profileStudy">Foundation</span></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const ageInput = document.getElementById('age');
            const levelSelect = document.getElementById('level');
            const avatars = document.querySelectorAll('.avatar');
            const submitBtn = document.getElementById('submitBtn');
            const generalAlert = document.getElementById('generalAlert');
            const ageAlert = document.getElementById('ageAlert');
            const generalAlertOkBtn = document.getElementById('generalAlertOkBtn');
            const ageAlertOkBtn = document.getElementById('ageAlertOkBtn');
            const userProfileCard = document.getElementById('userProfileCard');
            const validAgeIndicator = document.getElementById('validAgeIndicator');
            const invalidAgeIndicator = document.getElementById('invalidAgeIndicator');
            
            let selectedAvatar = null;
            
            // Set default avatar as selected
            avatars[0].classList.add('selected');
            selectedAvatar = avatars[0].getAttribute('data-avatar');
            document.getElementById('profileAvatar').src = avatars[0].src.replace('60x60', '80x80');
            
            // Avatar selection
            avatars.forEach(avatar => {
                avatar.addEventListener('click', function() {
                    // Remove selection from all avatars
                    avatars.forEach(a => a.classList.remove('selected'));
                    
                    // Add selection to clicked avatar
                    this.classList.add('selected');
                    selectedAvatar = this.getAttribute('data-avatar');
                    
                    // Update profile avatar
                    document.getElementById('profileAvatar').src = this.src.replace('60x60', '80x80');
                    
                    updateProfile();
                });
            });
            
            // Age validation
            ageInput.addEventListener('input', function() {
                const age = parseInt(this.value);
                
                if (age >= 18 && age <= 70) {
                    validAgeIndicator.style.display = 'inline';
                    invalidAgeIndicator.style.display = 'none';
                    this.style.borderColor = '#ddd';
                    document.getElementById('profileAge').textContent = age;
                } else {
                    validAgeIndicator.style.display = 'none';
                    invalidAgeIndicator.style.display = 'inline';
                    this.style.borderColor = 'red';
                }
            });
            
            // Level selection
            levelSelect.addEventListener('change', function() {
                document.getElementById('profileStudy').textContent = this.value;
            });
            
            // Submit button
            submitBtn.addEventListener('click', function() {
                if (!validateForm()) {
                    // First, show general validation message
                    generalAlert.style.display = 'flex';
                } else {
                    // If form is valid, show the profile card
                    updateProfile();
                    userProfileCard.style.display = 'block';
                }
            });
            
            // First alert OK button
            generalAlertOkBtn.addEventListener('click', function() {
                generalAlert.style.display = 'none';
                
                // Check specifically for age validation after dismissing first alert
                const age = parseInt(ageInput.value);
                if (ageInput.value === '' || isNaN(age) || age < 18 || age > 70) {
                    ageAlert.style.display = 'flex';
                }
            });
            
            // Second alert OK button
            ageAlertOkBtn.addEventListener('click', function() {
                ageAlert.style.display = 'none';
                ageInput.focus();
                
                // Force show the profile card after dismissing age alert
                userProfileCard.style.display = 'block';
            });
            
            // Form validation
            function validateForm() {
                const age = parseInt(ageInput.value);
                
                if (ageInput.value === '' || isNaN(age) || age < 18 || age > 70 || !selectedAvatar) {
                    return false;
                }
                
                return true;
            }
            
            // Update profile card
            function updateProfile() {
                const age = ageInput.value;
                const level = levelSelect.value;
                
                if (age && parseInt(age) >= 18 && parseInt(age) <= 70) {
                    document.getElementById('profileAge').textContent = age;
                }
                
                document.getElementById('profileStudy').textContent = level;
            }
        });
    </script>
</body>
</html>
