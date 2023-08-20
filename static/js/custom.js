function isValidName(name) {
    // Regular expression to match alphabetic characters and a minimum length of 2
    const namePattern = /^[A-Za-z]{2,}$/;
    return namePattern.test(name);
}
  
function validateNames() {
    const firstName = document.getElementById('id_first_name').value;
    const lastName = document.getElementById('id_last_name').value;
    const phoneNumber = document.getElementById('id_phone_number').value;
    const isValid = /^[\d\+\-\(\)\s]+$/.test(phoneNumber);
      if (!isValidName(firstName)) {
        alert('Please enter a valid first name.');
        return false;
      } else if (!isValidName(lastName)) {
        alert('Please enter a valid last name.');
        return false;
      } else if (!isValid) {
      alert('Invalid phone number format');
      return false;
      }
    return true;
}