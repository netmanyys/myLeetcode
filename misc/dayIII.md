Day III

1.    What is CSS?

      Cascading Style Sheets (CSS) is a style sheet language used for specifying the presentation and styling of a document written in a markup language such as HTML or XML
      CSS is a conrnerstone technology of the World Wide Web, alongside HTML and JavaScript
      CSS is designed to enable the separation of content and presentation, including layout, colors and fonts.

2.    How do you link a CSS file to an HTML document?

      use the <link> tag inside the <head> section of your HTML file. Here's how to do it:
      for example a CSS file
      ```css
      /* styles.css */
      body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
      }
      ```
      link the CSS File in your HTML
      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>My Web Page</title>
        <link rel="stylesheet" href="styles.css">
      </head>
      <body>
        <h1>Hello, world!</h1>
      </body>
      </html>
      ```
3.    What is block element? How is it different from inline, and inline-block elements?

      Definition:
      A block element takes up the full width available and starts on a new line.
      Common Block Elements:
      ```
      <div>
      <p>
      <h1> to <h6>
      <ul>, <ol>, <li>
      <section>, <article>
      ```
      a inline-block element does not start a new line and only takes up as much width as necessary
      Common Inline Elements:
      ```
      <span>
      <a>
      <strong>, <em>
      <img> (visually behaves like inline)
      ```

4.    What is the difference between pseudo-class and pseudo-element?
   
      A `pseudo-class` selects an element based on its state or behavior, not its position in the document tree.
      ```css
            /* Changes color when mouse hovers over a link */
      a:hover {
        color: red;
      }

      /* Styles the first child element */
      li:first-child {
        font-weight: bold;
      }

      ```
      common pseudo-classes: :hover, :focus, :nth-child(n), ::checked

      A `pseudo-element` targets and styles a specific part of an element, or creates a virtual element you can style.
      ```css
            /* Adds content before every paragraph */
      p::before {
        content: "📌 ";
      }

      /* Styles the first letter of a paragraph */
      p::first-letter {
        font-size: 2em;
        color: red;
      }

      ```
      common pseudo-elements: ::before, ::after, ::first-letter, ::first-line

5. Difference between child and descendant combinator?

> (child): selects direct children of an element.
  ```css
     div > p {
     color: red;
   }
  ```
  This styles only `<p>` tags that are immediately inside a `<div>`—not nested deeper.

> Space (descendant): selects all nested elements, no matter how deep.
  ```css
     div p {
     color: blue;
   }
  ```
> This styles all `<p>` tags inside a `<div>`, even if they’re nested inside other tags like `<section>` or `<article>`.

6. Two ways to make an element invisible & difference?

> display: none; — removes it from the layout.

> visibility: hidden; — it's invisible but still takes up space.

7. What’s the Box Model?
> Think of it like a box around every element:
> Content → Padding → Border → Margin

8. What’s !important used for?
> It forces a CSS rule to apply, even if other rules have more specificity.
> Used sparingly—mostly for overrides when nothing else works.

9. What does z-index do?
> Controls stacking order. Higher numbers appear on top of lower ones.

10. Can padding and margin be negative?

> Margin: yes, can be negative (pull elements closer).
> Padding: no, can’t be negative.

11. How to center a block element?
> margin: 0 auto;

```css
.centered-box {
  width: 300px;        /* Set a width */
  margin: 0 auto;      /* Top/bottom = 0, left/right = auto */
}

```
> This works because:

> Block elements take full width by default, so setting a specific width gives the browser room to center it.

> auto margins on the sides tell the browser to distribute leftover space evenly.

12.  What are grid items?
> Elements inside a CSS grid container.
> They can use properties like:

> grid-column, grid-row (for positioning)
> justify-self, align-self (for alignment)

13. What is a flex container?

> An element with display: flex;. It arranges children in a row or column.
Key properties:

- justify-content (horizontal alignment)
- align-items (vertical alignment)
- flex-wrap (wrap or not)

14.  Parent = 200px, child width: auto — what happens?

> Child’s width: fills all available space, so 200px.
> Margins: 0 by default (unless otherwise set).

15. Difference between px, em, and rem?
 >  -  px: fixed size.
 >  - em: relative to parent font size.
 >  - rem: relative to root (html) font size.

16. What is responsive web design?

  >  It makes your site look good on all screen sizes.
  It adapts to different screen perfectly like macbook, 
   mac, windows but also mobile phones



