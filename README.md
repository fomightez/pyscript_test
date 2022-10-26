## trying pyscript stuff


### What does work here

#### Pandas dataframe input and display

- In October 2022 I added examples using Pandas' `read_csv()` to get and render dataframes (also using panel for rendering) based on updated pyscript using py-config now. See `pandastest.html` ([on web here](https://fomightez.github.io/pyscript_test/pandastest.html)) and `csv_read_display_df_with_panel.html`  ([on web here](https://fomightez.github.io/pyscript_test/csv_read_display_df_with_panel.html)) and `csv_read_test.html`  ([on web here](https://fomightez.github.io/pyscript_test/csv_read_test.html)).


#### Markdown cells from notebook do work.

- Example with only markdown cells in a notebook based on the example of Eduardo Bonet

  **see [here](https://fomightez.github.io/pyscript_test/test_md_render.html) to see proof using [Eduoardo Bonet's approach](https://twitter.com/EduardoBonet/status/1521841937233465345) at least for now it renders markdown from notebooks just fine** (I had to remove the pyscript stuff because something was causing it to error out and not show markdown.)
  
  
#### REPL executing code

[direct_example.html](https://fomightez.github.io/pyscript_test/direct_example.html) is based on the example [this post](https://twitter.com/ericmjl/status/1520865845978746880) with the code from [this gist](https://gist.github.com/ericmjl/0e46f3810b7bac281ddc419176944483templates)


----------

### What sort of works here

- Code in Eduoardo's example notebook runs to generate a plot

[eduardo_sample_example.html](https://fomightez.github.io/pyscript_test/eduardo_sample_example.html) works to show plot being made from the code when you click the green arrow. However, it is supposed to also be showing markdown from the notebook being rendered and that is why same example is also udner 'What doesn't work here' (Note: it looks like [the posted example](https://twitter.com/ericmjl/status/1520865845978746880) though and so Eduardo Bonet who posted this example was also not seeing markdown rendered even though he tried to have the javascript handle that.). 
[Eduoardo Bonet's approach](https://twitter.com/EduardoBonet/status/1521841937233465345).  
Demonstrates numpy and matplotlib directly in a browser from static site.


-------------------------
### What doesn't work here

- Full example notebook of Eduardo Bonet with both code and markdown

[eduardo_sample_example.html](https://fomightez.github.io/pyscript_test/eduardo_sample_example.html) works to show plot being made from the code when you click the green arrow. However, it is supposed to also be showing markdown from the notebook being rendered. **It displays and works like from his site though!!** Go see it at https://eduardobonet.gitlab.io/nblite And so it isn't particular to GitHub and means he was seeing it have issues though. (By stripping out the pyscript stuff, I got the same approach to render markdown, see section 'Markdown cells from notebook do work.' and so it wasn't like it totally wasn't working. And in fact when it was failing to make markdown render fully, I'd see it render the markdown **for an instant** on hard refresh. And so this is probably a minor hurdle for those that know what they are doing and will get worked out soon. Note sometimes quickly entering inspection mode when trying to see what is messing up markdown rendering I'd note is showing inIt's showing in the 'Inspect' console that it is out of memory, specifically gives "WebAssembly module validated with warning: failed to allocate executable memory for module". But that didn't really seem to stop it from running the code other times when I gave it time.

