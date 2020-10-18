# Analyse the first website : <https://www.raywhite.com/>

## This website has some issues which are non-compliance to high accessibility standards :

1. The text is low contrast, which is hard for low-vision users to read.  Also, there are too many texts to read in the website and the font size is too small which is unfriendly to presbyopic users to read.
2. The "sign in or register" button is too small to press, so you have to tap that corner. If someone uses a screen reader or tablet PC, they would have trouble figuring out the association or just could not find this.
3. The element "footer.row" is not valid. ARIA roles must have valid values in order to perform their intended accessibility functions.
4. ARIA IDs are not unique. The value of an ARIA ID must be unique to prevent other instances from being overlooked by assistive technologies. 
5. Heading elements are not in a sequentially-descending order. Properly ordered headings that do not skip levels convey the semantic structure of the page, making it easier to navigate and understand when using assistive technologies.
6. `[user-scalable="no"]` is used in the `<meta name="viewport">` element or the `[maximum-scale]` attribute is less than 5. Disabling zooming is problematic for users with low vision who rely on screen magnification to properly see the contents of a web page. 
7. Some image elements do not have `[alt]` attributes when I read the source code. Informative elements should aim for short, descriptive alternate text.
8. Form elements do not have associated labels when I read the source code. Labels ensure that form controls are announced properly by assistive technologies, like screen readers.

## These are the steps I would take to rectify these issues :

1. I would change the text colour to make the text darker for low-vision users be easier to read and make the font size larger and divided the texts into different parts which can make presbyopic users be easier to read.

2. I would change the button size of  "sign in or register" to make it bigger for screen reader or tablet PC users to press or tap as well as be easier to find by users.

3. I would redefine the IDs of some elements to make it unique and change the code "footer.row" to make it valid.

4. I would make the heading elements are in a sequentially-descending order. Ordered headings make it easier for users or programmers to understand and navigate.

5. I would make zooming be able to use for users, because it's helpful for low-vision users to read and they can enlarge the page in order to make the text clear to read.

6. I would add `[alt]` attributes to those image elements which do not have `[alt]` attributes.  Adding alt can help users understand some information of these images and they should be short, descriptive.

7.  I would add associated labels to the form elements. This can help users to control the form when they use assistive tools.

   