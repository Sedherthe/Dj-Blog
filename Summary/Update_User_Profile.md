# Update User Profile

- **Model Forms**
   - Allows us to create form that work with a specific database model. 
   - We can update the details in a ModelForm using an instance of the model.
    - For example: `u_form = UserUpdateForm(instance=request.user)` would fill in the form with the current user details.
    
