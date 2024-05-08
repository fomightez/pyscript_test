## trying pyscript stuff


### What does work here

#### Pandas dataframe input and display

- In October 2022 (& later updated bokeh and panel tabulator use in early 2024) I added examples using Pandas' `read_csv()` to get and render dataframes (also using panel for rendering) based on updated pyscript using py-config now. See `pandastest.html` (working [on web here](https://fomightez.github.io/pyscript_test/pandastest.html)) and `csv_read_display_df_with_panel.html`  (working [on web here](https://fomightez.github.io/pyscript_test/csv_read_display_df_with_panel.html); stylistically it is most like the rendering of a Pandas dataframe in Jupyter) and `csv_read_test.html`  (working [on web here](https://fomightez.github.io/pyscript_test/csv_read_test.html)) and `csv_read_from_same_location.html` (working [on web here](https://fomightez.github.io/pyscript_test/csv_read_from_same_location.html)). In March 2024, I added a very streamlined version to demonstrate getting the CSV file using the `[files]` key use as described [here](https://stackoverflow.com/a/78049663/8508004) and [here](https://jeff.glass/post/whats-new-pyscript-2023-11-1/#config). [code](https://github.com/fomightez/pyscript_test/blob/main/csv_Mar_2024_files_key_test.html) . [Demo link](https://fomightez.github.io/pyscript_test/csv_Mar_2024_files_key_test.html). I also added a streamlined version using the `[[fetch]]` feature that removes the need to rely on `open_url` directly and adds the `from` key to specify location for fetching, see [here](https://stackoverflow.com/a/76148659/8508004). That is `csv_Mar_2024_fetch_test.html` (working [on web here](https://fomightez.github.io/pyscript_test/csv_Mar_2024_fetch_test.html)). These two approaches, with `[files]` and `[[fetch]]`, (with the `[files]` method currently favored going forward) are meant to supercede the `open_url` method, which is illustated in the April 2023 streamlined demonstration getting the CSV file that uses `open_url` (which curiosuly the current demos still seem to use), see  `csv_apr_2023_test.html` (working [on web here](https://fomightez.github.io/pyscript_test/csv_apr_2023_test.html)).


- I added the CSV retrieval example based on `[files]` key use as described [here](https://stackoverflow.com/a/78049663/8508004) and [here](https://jeff.glass/post/whats-new-pyscript-2023-11-1/#config). [code](https://github.com/fomightez/pyscript_test/blob/main/csv_Mar_2024_files_key_test.html) . [Demo link](https://fomightez.github.io/pyscript_test/csv_Mar_2024_files_key_test.html). It didn't seem to work, like the `[[fetch]]` one does. I think I need a better example for this. The ones in the current (March 2024) examples don't seem to use this and still use the older `open_url` approach, despite what was said [here](https://stackoverflow.com/a/76148659/8508004) in May 2023 about `[[fetch]]` that pre-dates `[files]`.

#### Matplotlib plot examples

- In April 2023, I added Matplotlib example from https://pyscript.net/examples/matplotlib.html in start of effort to update plots to current ways. See `matplotlib.html)` (working on web [here](https://fomightez.github.io/pyscript_test/matplotlib.html)).
- Based on the April 2023 update of the Matplotlib and the old version, I updated the `plot_example.html` (working [on web here](https://fomightez.github.io/pyscript_test/plot_example.html)).
- Based on the April 2023 update of the Matplotlib and [my reply to a Stackoverflow post](https://stackoverflow.com/a/76016831/8508004), I added another matplotlib example, `another_plot_example.html` (working [on web here](https://fomightez.github.io/pyscript_test/another_plot_example.html)).


#### Markdown cells from notebook do work.

- Example with only markdown cells in a notebook based on the example of Eduardo Bonet

  **see [here](https://fomightez.github.io/pyscript_test/test_md_render.html) to see proof using [Eduoardo Bonet's approach](https://twitter.com/EduardoBonet/status/1521841937233465345) at least for now it renders markdown from notebooks just fine** (I had to remove the pyscript stuff because something was causing it to error out and not show markdown.)
  
  
#### REPL executing code / and Terminals

- REPL page with older pyscript: [direct_example.html](https://fomightez.github.io/pyscript_test/direct_example.html) is based on the example [this post](https://twitter.com/ericmjl/status/1520865845978746880) with the code from [this gist](https://gist.github.com/ericmjl/0e46f3810b7bac281ddc419176944483templates)

- terminal page: [terminal_page based on November '23 and early 2024 changes](https://fomightez.github.io/pyscript_test/REPL_march_2024.html)  terminal based on [code for a terminal supplied here](https://github.com/JeffersGlass/pyscript/tree/84f197b657a6fae5573b1b8b11b2dad1a05f5531); I had hoped to make an interactive REPL like the code in an article detailing ['What's New in PyScript Next (2023.11.1')](https://jeff.glass/post/whats-new-pyscript-2023-11-1/). Things have changed:
    > "PyScript no longer imports any names into the Python namespace for you. This differs from the previous release, where the names js, pyscript, Element, display, and HTML were treated a bit like builtins, and imported prior to any user-written code."
    And I was hoping the new interactive REPL would be helpful finding things like `Element` so that I can import it. However, the interactive version failed to work like in the documentation or that article with either the 2023.11.2 or 2024.3.2 pyscript code. Or at least failed in my attempts so far.


----------

### What sort of works here

- Code in Eduoardo's example notebook runs to generate a plot

[eduardo_sample_example.html](https://fomightez.github.io/pyscript_test/eduardo_sample_example.html) works to show plot being made from the code when you click the green arrow. However, it is supposed to also be showing markdown from the notebook being rendered and that is why same example is also udner 'What doesn't work here' (Note: it looks like [the posted example](https://twitter.com/ericmjl/status/1520865845978746880) though and so Eduardo Bonet who posted this example was also not seeing markdown rendered even though he tried to have the javascript handle that.). 
[Eduoardo Bonet's approach](https://twitter.com/EduardoBonet/status/1521841937233465345).  
Demonstrates numpy and matplotlib directly in a browser from static site.

- Plotly example makes a plot using Plotly graph objects

Based on update that doesn't allow `print()`, see [here](https://docs.pyscript.net/latest/reference/API/display.html), and [my reply to a Stackoverflow post](https://stackoverflow.com/q/76187420/8508004). The line plot, actually scatter, using Plotly graph objects works and displays but nothing happens if you click on it, which was what the OP at Stackoverflow was seeking. OP was using Plotly Express which I' not sure even works with Plotly's `.on_click()` method. 

-------------------------
### What doesn't work here



- 'open_cv_demo.html' Got stuck on getting an image from URL so that I could use openCV / CV2 to manipulate it. This was starting point of an attempt to extend what I was able to do with Pyodide in JupyterLite to pyscript, see [here](https://stackoverflow.com/questions/74533570/pyscript-modulenotfounderror-no-module-named-cv2#comment131573724_74533570). ([This](https://jeff.glass/post/pyscript-image-upload/) may have helped but I didn't note consulting it in code and near the end I thought I was using some of it but still no luck.)
I got stuck on trying to read in the image from URL. I need to locate an example that is current and working.  
I think once I got image read in I could pass the contents to numpy as an array and then cv2 can use it. I'll keep my eyes open for a modern example.  
See the history for the many things I tried.

- Full example notebook of Eduardo Bonet with both code and markdown

[eduardo_sample_example.html](https://fomightez.github.io/pyscript_test/eduardo_sample_example.html) works to show plot being made from the code when you click the green arrow. However, it is supposed to also be showing markdown from the notebook being rendered. **It displays and works like from his site though!!** Go see it at https://eduardobonet.gitlab.io/nblite And so it isn't particular to GitHub and means he was seeing it have issues though. (By stripping out the pyscript stuff, I got the same approach to render markdown, see section 'Markdown cells from notebook do work.' and so it wasn't like it totally wasn't working. And in fact when it was failing to make markdown render fully, I'd see it render the markdown **for an instant** on hard refresh. And so this is probably a minor hurdle for those that know what they are doing and will get worked out soon. Note sometimes quickly entering inspection mode when trying to see what is messing up markdown rendering I'd note is showing inIt's showing in the 'Inspect' console that it is out of memory, specifically gives "WebAssembly module validated with warning: failed to allocate executable memory for module". But that didn't really seem to stop it from running the code other times when I gave it time.

