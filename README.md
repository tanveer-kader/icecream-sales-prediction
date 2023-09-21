# icecream-sales-prediction

## Follow these steps to run it on your machine

1. clone this repository
2. open anaconda navigator
3. Launch spyder
4. on top right side:

   - click folder icon (if you hover you will see "browse a working directory")
   - locate where you cloned the repository and select it

5. double click to open the file named "icecream_sales_webapp.py" - it will show up the codes
6. change the file directory on line 13 and 14. pickle.load(open("path-on-your-machine/icecream_sale_lr_model.sav", "rb"))
7. To find the path:

   - on the right side where all the files are displayed, you can "right click" on file (icecream_sale_lr_model.sav) and click on "copy absolute path"
   - paste to replace the path as shown in point 6 "path on your machine"
   - do this for both models

8. save it
9. go to anaconda navigator:

   - click on environments
   - left click on "the green play button"
   - click on "open terminal"

10. run this command below:

    - streamlit run "path-on-your-machine/icecream_sales_webapp.py"

11. Your default browser will open up and ready to use the app.
