# How to Add Yourself to the Lab Page

1. **Fork the repository**  
   Please fork this repository on GitHub. After forking, clone your fork to your local machine.

2. **Add your photo**  
   On your local machine, add your image file to `yzhao062.github.io/images/others/`. Use a small size square image if possible. A webp format file is preferred.  
   For example: peilin.webp

3. **Update the lab.html file**  
Open `lab.html` in your text editor. Find the section where team members are listed.  
Insert a block of code similar to the one below, and replace "Peilin Cai" and other details with your own.  
Insert your block in alphabetical order by last name.

For example:  
```html
<!-- Team Member -->
<div class="col-md-4 col-sm-6 team-member">
    <img src="images/others/peilin.webp" alt="Peilin Cai" class="team-img">
    <h3><a href="https://viterbi-web.usc.edu/~yzhao010/lab.html">Peilin Cai</a></h3>
    <p>Multimodal/Generative AI</p>
    <p class="member-status">Master Student (peilinca@usc.edu)</p>
</div>




4. **Render the page locally**
Open lab.html in your browser to see if your changes look correct. If you want to run a local server, try PyCharm

5. **Commit, push, and submit a pull request**
Once you are satisfied with the changes, commit them to your forked repository and push.
Finally, submit a pull request to the main repository.
