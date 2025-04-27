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
            /* Changed from display: none to block */
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
                    <input type="hidden" id="selectedAvatar" name="selectedAvatar">
                </div>
                
                <button type="submit" class="submit-btn" id="submitProfile">Submit Profile</button>
            </form>
        </div>
        
        <!-- Profile card is now visible by default -->
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
            selectedAvatarInput.value = '1';
            
            // Username validation
            usernameInput.addEventListener('input', function() {
                const value = this.value;
                
                // Clear previous messages
                usernameError.style.display = 'none';
                usernameSuccess.style.display = 'none';
                
                if (value.length === 0) {
                    // Empty input, do nothing
                    profileName.textContent = '[Your Name]';
                    return;
                }
                
                if (value.length !== 7) {
                    usernameError.textContent = 'Username must be 7 characters long, starting with "w"';
                    usernameError.style.display = 'block';
                    profileName.textContent = value;
                    return;
                }
                
                if (!value.startsWith('w')) {
                    usernameError.textContent = 'Username must start with "w"';
                    usernameError.style.display = 'block';
                    profileName.textContent = value;
                    return;
                }
                
                // Valid username
                usernameSuccess.style.display = 'block';
                
                // Update profile card in real-time
                profileName.textContent = value;
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
                    
                    // Update profile card in real-time
                    profileAvatar.src = this.src;
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
                
                // Show success alert instead of just updating the profile card
                // (since the profile card is already visible and updated in real-time)
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
            /* Changed from display: none to display: block to show profile initially */
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
                        <img src="https://via.placeholder.com/150/9B5DE5/FFFFFF?text=1" class="avatar" data-avatar="1" alt="Avatar 1">
                        <img src="https://via.placeholder.com/150/F15BB5/FFFFFF?text=2" class="avatar" data-avatar="2" alt="Avatar 2">
                        <img src="https://via.placeholder.com/150/FEE440/000000?text=3" class="avatar" data-avatar="3" alt="Avatar 3">
                    </div>
                    <input type="hidden" id="selectedAvatar" name="selectedAvatar">
                </div>
                
                <button type="submit" class="submit-btn" id="submitProfile">Submit Profile</button>
            </form>
        </div>
        
        <!-- Profile card is now visible by default -->
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
            
            // Set default avatar
            selectedAvatarInput.value = "1";
            
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
                
                // Update profile card in real-time
                profileName.textContent = value;
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
                    
                    // Update profile card in real-time
                    profileAvatar.src = this.src;
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
                
                // Update profile card
                profileName.textContent = username;
                profileAge.textContent = age;
            });
            
            // Close alert popup
            alertOkBtn.addEventListener('click', function() {
                alertPopup.style.display = 'none';
            });
            
            // Real-time updates for profile card as user interacts with form
            usernameInput.addEventListener('input', updateProfileCard);
            avatars.forEach(avatar => {
                avatar.addEventListener('click', updateProfileCard);
            });
            
            function updateProfileCard() {
                const username = usernameInput.value;
                const age = document.getElementById('age').value;
                
                if (username) {
                    profileName.textContent = username;
                } else {
                    profileName.textContent = '[Your Name]';
                }
                
                profileAge.textContent = age;
            }
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
            /* Changed from 'display: none' to 'display: block' to make it visible by default */
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
            
            // Initialize profile name with username value
            profileName.textContent = usernameInput.value;
            
            // Set default profile study level
            profileStudy.textContent = studyLevelSelect.value;
            
            // Default avatar selection
            selectedAvatarInput.value = "1"; // Default to first avatar
            
            // Age validation
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
                
                // Update profile card in real-time
                profileAge.textContent = ageValue;
            });
            
            // Study level selection
            studyLevelSelect.addEventListener('change', function() {
                // Update profile card in real-time
                profileStudy.textContent = this.value;
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
                    
                    // Update profile card in real-time
                    profileAvatar.src = this.src;
                });
            });
            
            // Form submission
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
                
                // Profile card is already visible by default, so we don't need to show it
                // Just update it with final values
                profileName.textContent = usernameInput.value;
                profileAge.textContent = age;
                profileStudy.textContent = studyLevel;
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
            
            <!-- Profile Card (Visible initially with real user data) -->
            <div class="profile-card" id="profileCard">
                <h2>Your Profile</h2>
                <div class="profile-image">
                    <img src="https://picsum.photos/200" alt="Profile Image" id="profileImage">
                </div>
                <p><strong id="cardName">Oliver Brown</strong></p>
                <p>Study: <span id="cardStudy">FT UG student</span></p>
                <p>Subscription: <span id="cardSubscription">Standard £9.99 per/month</span></p>
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
            
            // Update when age changes
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
            
            // Handle form submission
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Update the profile card with form values
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
            
            // Initialize profile with form values
            cardName.textContent = document.getElementById('userName').value;
            cardStudy.textContent = studyStatus.value;
            cardSubscription.textContent = subscription.value;
            
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
            max-width: 800px;
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
            margin-bottom: 30px;
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
        }

        .verification h3 {
            margin-bottom: 10px;
            color: #333;
        }

        .math-challenge {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .math-challenge span {
            margin: 0 5px;
        }

        .math-challenge input {
            width: 60px;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .verify-btn {
            background-color: #4c72af;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }

        .verify-btn:hover {
            background-color: #3a5a8a;
        }

        .verification-message {
            margin-top: 10px;
            padding: 10px;
            border-radius: 4px;
            font-weight: bold;
            display: none;
        }

        .verification-success {
            background-color: #d4edda;
            color: #155724;
        }

        .verification-error {
            background-color: #f8d7da;
            color: #721c24;
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
            overflow: hidden;
            margin-right: 20px;
            background-color: #f1f1f1;
        }

        .profile-image img {
            width: 100%;
            height: auto;
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
        }

        .customization-section h2 {
            margin-bottom: 15px;
            color: #333;
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
            border: 2px solid #69b578;
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
            
            <!-- Form Section -->
            <div class="form-section">
                <h2>User Details</h2>
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
                            <option value="International tuition fee £17,000">International tuition fee £17,000</option>
                            <option value="Home student fee £9,250">Home student fee £9,250</option>
                            <option value="EU student fee £13,000">EU student fee £13,000</option>
                        </select>
                    </div>
                    
                    <!-- Human Verification Section -->
                    <div class="verification">
                        <h3>Verify you are human</h3>
                        <div id="mathChallenge" class="math-challenge">
                            <span id="num1">5</span>
                            <span>+</span>
                            <span id="num2">3</span>
                            <span>=</span>
                            <input type="number" id="userAnswer" min="0">
                        </div>
                        <button type="button" id="verifyBtn" class="verify-btn">Click to Verify</button>
                        <div id="verificationSuccess" class="verification-message verification-success">
                            Correct! You may now submit your profile.
                        </div>
                        <div id="verificationError" class="verification-message verification-error">
                            Incorrect. Try again.
                        </div>
                    </div>
                    
                    <button type="submit" id="submitProfile" class="submit-btn">Submit Profile</button>
                </form>
            </div>
            
            <!-- Profile Card (Hidden initially) -->
            <div class="profile-card" id="profileCard">
                <h2>Your Profile</h2>
                <div class="profile-details">
                    <div class="profile-image">
                        <img src="https://picsum.photos/seed/profile/200" alt="Profile Image" id="profileImage">
                    </div>
                    <div class="profile-info">
                        <h3 id="cardName">Tom Boyle</h3>
                        <p>Study: <span id="cardStudy">FT UG student</span></p>
                        <p>Tuition Fees: <span id="cardTuitionFees">International tuition fee £17,000</span></p>
                    </div>
                </div>
            </div>
            
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
    
    <!-- Confirmation Dialog -->
    <div class="dialog-overlay" id="confirmDialog">
        <div class="dialog">
            <p id="dialogText">This page says</p>
            <div class="dialog-buttons">
                <button class="dialog-btn cancel-btn" id="cancelBtn">Cancel</button>
                <button class="dialog-btn ok-btn" id="okBtn">OK</button>
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
            const tuitionFees = document.getElementById('tuitionFees');
            const profileContainer = document.getElementById('profileContainer');
            const patternOptions = document.querySelectorAll('.pattern-option');
            const verifyBtn = document.getElementById('verifyBtn');
            const userAnswer = document.getElementById('userAnswer');
            const verificationSuccess = document.getElementById('verificationSuccess');
            const verificationError = document.getElementById('verificationError');
            const submitBtn = document.getElementById('submitProfile');
            const confirmDialog = document.getElementById('confirmDialog');
            const dialogText = document.getElementById('dialogText');
            const okBtn = document.getElementById('okBtn');
            const cancelBtn = document.getElementById('cancelBtn');
            
            // Generate random math challenge
            let num1 = Math.floor(Math.random() * 10) + 1;
            let num2 = Math.floor(Math.random() * 10) + 1;
            document.getElementById('num1').textContent = num1;
            document.getElementById('num2').textContent = num2;
            
            // Verify human check
            verifyBtn.addEventListener('click', function() {
                const correctAnswer = num1 + num2;
                const userAnswerValue = parseInt(userAnswer.value);
                
                if (userAnswerValue === correctAnswer) {
                    verificationSuccess.style.display = 'block';
                    verificationError.style.display = 'none';
                    submitBtn.style.display = 'block'; // Show submit button after successful verification
                    
                    // Show confirmation dialog
                    showDialog("This page says", "Correct! You may now submit your profile.");
                } else {
                    verificationSuccess.style.display = 'none';
                    verificationError.style.display = 'block';
                    submitBtn.style.display = 'none'; // Hide submit button if verification fails
                    
                    // Show error dialog
                    showDialog("This page says", "Incorrect. Try again.");
                }
            });
            
            // Handle form submission
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Update the profile card with form values
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
            
            // Dialog functions
            function showDialog(title, message) {
                dialogText.textContent = message;
                confirmDialog.style.display = 'flex';
            }
            
            okBtn.addEventListener('click', function() {
                confirmDialog.style.display = 'none';
            });
            
            cancelBtn.addEventListener('click', function() {
                confirmDialog.style.display = 'none';
            });
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
        }

        .container {
            width: 90%;
            max-width: 800px;
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
        }

        .verification h3 {
            margin-bottom: 10px;
            color: #333;
        }

        .math-challenge {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .math-challenge span {
            margin: 0 5px;
        }

        .math-challenge input {
            width: 60px;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .verify-btn {
            background-color: #4c72af;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }

        .verify-btn:hover {
            background-color: #3a5a8a;
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
            overflow: hidden;
            margin-right: 20px;
            background-color: #f1f1f1;
        }

        .profile-image img {
            width: 100%;
            height: auto;
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
            border: 2px solid #69b578;
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

        .success-message {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 4px;
            margin-top: 10px;
            display: none;
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
            
            <!-- Form Section -->
            <div class="form-section">
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
                            <option value="Premium £14.99 per/month">Premium £14.99 per/month</option>
                            <option value="Basic £4.99 per/month">Basic £4.99 per/month</option>
                        </select>
                    </div>
                    
                    <!-- Human Verification Section -->
                    <div class="verification">
                        <h3>Verify you are human</h3>
                        <button type="button" id="verifyBtn" class="verify-btn">Click to Verify</button>
                    </div>
                    
                    <div class="success-message" id="successMessage"></div>
                    
                    <button type="submit" id="submitProfile" class="submit-btn">Submit Profile</button>
                </form>
            </div>
            
            <!-- Profile Card (Hidden initially) -->
            <div class="profile-card" id="profileCard">
                <h2>Your Profile</h2>
                <div class="profile-details">
                    <div class="profile-image">
                        <img src="https://picsum.photos/seed/samprofile/200" alt="Profile Image" id="profileImage">
                    </div>
                    <div class="profile-info">
                        <h3 id="cardName">Sam Patel</h3>
                        <p>Study: <span id="cardStudy">FT UG student</span></p>
                        <p>Subscription: <span id="cardSubscription">Standard £9.99 per/month</span></p>
                    </div>
                </div>
            </div>
            
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
            const cardName = document.getElementById('cardName');
            const cardStudy = document.getElementById('cardStudy');
            const cardSubscription = document.getElementById('cardSubscription');
            const subscription = document.getElementById('subscription');
            const profileContainer = document.getElementById('profileContainer');
            const patternOptions = document.querySelectorAll('.pattern-option');
            const verifyBtn = document.getElementById('verifyBtn');
            const submitBtn = document.getElementById('submitProfile');
            const successMessage = document.getElementById('successMessage');
            
            // Dialog elements
            const mathDialog = document.getElementById('mathDialog');
            const successDialog = document.getElementById('successDialog');
            const userAnswer = document.getElementById('userAnswer');
            const okMathBtn = document.getElementById('okMathBtn');
            const cancelMathBtn = document.getElementById('cancelMathBtn');
            const okSuccessBtn = document.getElementById('okSuccessBtn');
            const successText = document.getElementById('successText');
            
            // Generate random math challenge
            let num1 = Math.floor(Math.random() * 10) + 1;
            let num2 = Math.floor(Math.random() * 10) + 1;
            document.getElementById('num1').textContent = num1;
            document.getElementById('num2').textContent = num2;
            
            // Open verification dialog
            verifyBtn.addEventListener('click', function() {
                mathDialog.style.display = 'flex';
                userAnswer.focus();
            });
            
            // Handle math verification
            okMathBtn.addEventListener('click', function() {
                const correctAnswer = num1 + num2;
                const userAnswerValue = parseInt(userAnswer.value);
                
                mathDialog.style.display = 'none';
                
                if (userAnswerValue === correctAnswer) {
                    // Show success dialog
                    successDialog.style.display = 'flex';
                    successText.textContent = "Correct! You may now submit your profile.";
                    
                    // Enable submit button
                    submitBtn.style.display = 'block';
                    successMessage.textContent = "Correct! You may now submit your profile.";
                    successMessage.style.display = 'block';
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
            
            // Handle form submission
            profileForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Update the profile card with form values
                cardSubscription.textContent = subscription.value;
                
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

Scenario7---------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Your Profile</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 600px;
            background-color: #e6e0e0;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        .profile-info {
            background-color: #f9f3f0;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }

        .highlighted-info {
            border: 2px solid #8bc34a;
            border-radius: 25px;
            padding: 10px;
            margin-bottom: 15px;
            background-color: #f9f9f9;
        }

        .user-details {
            background-color: #fffef2;
            padding: 15px;
            border-radius: 8px;
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
        }

        .avatar-selection {
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
            justify-content: center;
        }

        .avatar {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.2s ease;
            opacity: 0.8;
        }

        .avatar:hover {
            transform: scale(1.05);
        }

        .avatar.selected {
            transform: scale(1.1);
            border: 3px solid #8bc34a;
            opacity: 1;
            box-shadow: 0 0 10px rgba(139, 195, 74, 0.5);
        }

        .btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #8bc34a;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #7cb342;
        }

        .error-message {
            color: #f44336;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }

        .valid-indicator {
            color: #4CAF50;
            font-size: 14px;
            margin-left: 5px;
            display: none;
        }

        .alert-box {
            position: relative;
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #f44336;
            border-radius: 4px;
            background-color: #fff;
            color: #333;
            display: none;
        }

        .alert-box.show {
            display: block;
        }

        .alert-icon {
            color: #f44336;
            margin-right: 10px;
        }

        .ok-btn {
            background-color: #8bc34a;
            color: white;
            border: none;
            padding: 5px 15px;
            border-radius: 4px;
            cursor: pointer;
            position: absolute;
            right: 10px;
            bottom: 10px;
        }

        /* Profile card styles */
        .profile-card-container {
            display: none;
            margin-top: 20px;
            background-color: #e6e0e0;
            padding: 20px;
            border-radius: 8px;
        }

        .profile-card {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            border: 2px solid #8bc34a;
        }

        .profile-avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-right: 20px;
        }

        .profile-details {
            flex: 1;
        }

        .profile-details p {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Create Your Profile</h1>
        
        <!-- Student Info Box -->
        <div class="profile-info highlighted-info">
            <p><strong>Student Full Name</strong></p>
            <p><strong>Student ID:</strong> w1234567</p>
            <p><strong>The course you study</strong></p>
        </div>
        
        <!-- User Details Form -->
        <div class="user-details">
            <div class="form-group">
                <label for="username">UserName:</label>
                <input type="text" id="username" value="wminComp" readonly>
            </div>
            
            <div class="form-group">
                <label for="age">Your Age:</label>
                <input type="number" id="age" min="18" placeholder="Min value 18">
                <span class="error-message" id="age-error">✗ Age must be between 18 and 70!</span>
                <span class="valid-indicator" id="age-valid">✓ Valid Age</span>
            </div>
            
            <div class="form-group">
                <label for="level">The level you study:</label>
                <select id="level">
                    <option value="Foundation" selected>Foundation</option>
                    <option value="Undergraduate">Undergraduate</option>
                    <option value="Postgraduate">Postgraduate</option>
                </select>
            </div>
            
            <div class="form-group">
                <label>Select an Avatar:</label>
                <div class="avatar-selection">
                    <img src="https://cdn-icons-png.flaticon.com/512/219/219969.png" class="avatar" data-id="1" alt="Avatar 1">
                    <img src="https://cdn-icons-png.flaticon.com/512/219/219983.png" class="avatar" data-id="2" alt="Avatar 2">
                    <img src="https://cdn-icons-png.flaticon.com/512/219/219988.png" class="avatar" data-id="3" alt="Avatar 3">
                </div>
            </div>
            
            <button class="btn" id="submit-profile">Submit Profile</button>
        </div>
        
        <!-- Alert Box -->
        <div class="alert-box" id="alert-box">
            <p><span class="alert-icon">⚠️</span> Please fill all required fields before submitting.</p>
            <button class="ok-btn" id="ok-btn">OK</button>
        </div>
        
        <!-- Profile Card (Shows after submission) -->
        <div class="profile-card-container" id="profile-card-container">
            <h2>Your Profile</h2>
            <div class="profile-card">
                <img src="" id="profile-avatar" class="profile-avatar" alt="Selected Avatar">
                <div class="profile-details">
                    <p><strong>UserName:</strong> <span id="profile-username">wminComp</span></p>
                    <p><strong>Age:</strong> <span id="profile-age"></span></p>
                    <p><strong>Study:</strong> <span id="profile-level"></span></p>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Elements
            const ageInput = document.getElementById('age');
            const levelSelect = document.getElementById('level');
            const avatars = document.querySelectorAll('.avatar');
            const submitBtn = document.getElementById('submit-profile');
            const alertBox = document.getElementById('alert-box');
            const okBtn = document.getElementById('ok-btn');
            const ageError = document.getElementById('age-error');
            const ageValid = document.getElementById('age-valid');
            const profileCardContainer = document.getElementById('profile-card-container');
            
            // Profile card elements
            const profileAvatar = document.getElementById('profile-avatar');
            const profileAge = document.getElementById('profile-age');
            const profileLevel = document.getElementById('profile-level');
            
            // Variables
            let selectedAvatar = null;
            
            // Functions
            function validateAge(age) {
                return age >= 18 && age <= 70;
            }
            
            function updateProfileCard() {
                if (selectedAvatar && validateAge(ageInput.value)) {
                    profileAvatar.src = selectedAvatar.src;
                    profileAge.textContent = ageInput.value;
                    profileLevel.textContent = levelSelect.value;
                    profileCardContainer.style.display = 'block';
                }
            }
            
            function checkFormValidity() {
                return selectedAvatar && validateAge(ageInput.value);
            }
            
            // Event Listeners
            // Avatar selection
            avatars.forEach(avatar => {
                avatar.addEventListener('click', function() {
                    // Remove selected class from all avatars
                    avatars.forEach(a => a.classList.remove('selected'));
                    
                    // Add selected class to clicked avatar
                    this.classList.add('selected');
                    selectedAvatar = this;
                    
                    // If age is valid, automatically update profile card
                    if (validateAge(ageInput.value)) {
                        updateProfileCard();
                    }
                });
            });
            
            // Age validation
            ageInput.addEventListener('input', function() {
                const age = parseInt(this.value);
                
                if (validateAge(age)) {
                    ageError.style.display = 'none';
                    ageValid.style.display = 'inline';
                    
                    // If avatar is selected, automatically update profile card
                    if (selectedAvatar) {
                        updateProfileCard();
                    }
                } else {
                    ageError.style.display = 'inline';
                    ageValid.style.display = 'none';
                }
            });
            
            // Level selection change
            levelSelect.addEventListener('change', function() {
                // If avatar is selected and age is valid, automatically update profile card
                if (selectedAvatar && validateAge(ageInput.value)) {
                    updateProfileCard();
                }
            });
            
            // Submit button
            submitBtn.addEventListener('click', function() {
                if (checkFormValidity()) {
                    updateProfileCard();
                } else {
                    alertBox.style.display = 'block';
                }
            });
            
            // OK button in alert box
            okBtn.addEventListener('click', function() {
                alertBox.style.display = 'none';
            });
            
            // Set Foundation as default
            levelSelect.value = 'Foundation';
        });
    </script>
</body>
</html>
