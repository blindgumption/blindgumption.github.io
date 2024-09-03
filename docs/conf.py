# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BlindGumption GitHub Pages'
copyright = '2024, Joel Dodson'
author = 'Joel Dodson'
##
# Do not version the docs for now
# cannot figure out how to keep the 'book' theme from showing the version 
# release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_book_theme"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ["_static"]

# links for the sphinx_book_theme
# the 'book' theme is based on the 'pydata' theme thus options derive from there as well.
# pdata-sphinx-theme opsions: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/layout.html#references
# sphinx-book-theme options: https://sphinx-book-theme.readthedocs.io/en/latest/reference.html

html_theme = "sphinx_book_theme"
html_theme_options = {
    "use_download_button": False,
    "repository_url": "https://github.com/blindgumption/blindgumption.github.io",
    "use_repository_button": True,
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "show_version_warning_banner": False,
}
