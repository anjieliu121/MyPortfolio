from shiny.ui import modal_show, modal, modal_button
from htmltools import TagList, tags

########################################################################################################################
# Cosmology
########################################################################################################################
cosmo_about_text = TagList(
    tags.br(),
    tags.br(),
    tags.h5("About", style="font-weight: bold;"),
    tags.p(
        """
        This is a visual demonstration of the research on investigating the 
        significance of properties of gas profiles of dark matter halos across the scales
        with the aid of statistical and machine learning models.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

cosmo_dataset_information = TagList(
    tags.h5("Data Description", style="font-weight: bold;"),
    tags.p(
        """
        The data comes from the 
        """,
        tags.a("IllustrisTNG", href=("https://www.tng-project.org"), target="_blank"),
        """ project, large-scale cosmological galaxy formation simulations.
        This study uses the TNG300 dataset with a resolution of 1 and a redshift of 0. """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.hr(),
    tags.h5("Data Size", style="font-weight: bold;"),
    tags.ul(
            tags.li(
                tags.p("""Gas Data: 3733 observations * 30 attributes * 57 groups"""),
            ),
            tags.li(
                tags.p("""Galaxy Data: 1146 observations * 25 properties"""),
            ),
    ),
)

########################################################################################################################
# Sustainability
########################################################################################################################
co2_about_text = TagList(
    tags.br(),
    tags.br(),
    tags.h5("About", style="font-weight: bold;"),
    tags.p(
        """
        This is a 
        """,
        tags.a("public interactive dashboard", href=("https://anjie-liu.shinyapps.io/sustainability-world-map/"), target="_blank"),
        """
         visualizing the global CO2 emission.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

co2_dataset_information = TagList(
    tags.h5("Data Description", style="font-weight: bold;"),
    tags.p(
        """
        The dataset can be found on  
        """,
        tags.a("Kaggle", href=("https://www.kaggle.com/datasets/ulrikthygepedersen/co2-emissions-by-country"), target="_blank"),
        """ project, large-scale cosmological galaxy formation simulations.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),

    tags.h5("Data Size", style="font-weight: bold;"),
    tags.ul(
            tags.li(
                tags.p("""13954 observations * 4 variables"""),
            ),
    ),
    tags.hr(style="margin: 10px;"),
    tags.h5("Inspiration", style="font-weight: bold;"),
    tags.p(
        """The 2023 \"Hack the future\" hackathon strives for eco-friendly solutions.
        This public webpage aims for educating the general public and increasing the public
        awareness on the greenhouse gas issue."""
    )
)

########################################################################################################################
# Housing
########################################################################################################################
house_about_text = TagList(
    tags.br(),
    tags.br(),
    tags.h5("About", style="font-weight: bold;"),
    tags.p(
        """
        This is a 
        """,
        tags.a("public interactive dashboard", href=("https://racial-disparity-index-tool.streamlit.app/")),
        """
         exploring the individuals' socioeconomic characteristics and their likelihood of homeownership.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

house_dataset_information = TagList(
    tags.h5("Data Description", style="font-weight: bold;"),
    tags.p(
        """
        The PUMA dataset is pulled using the tidycensus package in R. 
        It's an API from the Census.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),


    tags.hr(),
    tags.h5("Contribution", style="font-weight: bold;"),
    tags.p(
        """
        I maintained the dashboard during the summer of 2023.
        """
    )
)


########################################################################################################################
# Well Production
########################################################################################################################
well_about_text = TagList(
    tags.br(),
    tags.br(),
    tags.h5("About", style="font-weight: bold;"),
    tags.p(
        """
        This is a demonstration of the research on optimizing completion's sequence of well production
        using tuned machine learning models.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

well_dataset_information = TagList(
    tags.h5("Data Description", style="font-weight: bold;"),
    tags.p(
        """
        The dataset is provided by ConocoPhillips.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.hr(),

    tags.h5("Data Size", style="font-weight: bold;"),
    tags.ul(
        tags.li(
            tags.p("""10857 wells * 22 properties"""),
        ),
    ),
    tags.hr(),

    tags.h5("Paper", style="font-weight: bold;"),
    tags.p(
        """
        Check out the 
        """,
        tags.a("draft", href=("https://drive.google.com/file/d/1Pg1gobIy0i2OVwnY87LIIuUK5miDwqSL/view?usp=sharing")),
        """
        that will soon be submitted to 
        """,
        tags.a("arXiv", href=("https://arxiv.org")),

        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

########################################################################################################################
# Real Estate
########################################################################################################################
real_about_text = TagList(
    tags.br(),
    tags.br(),
    tags.h5("About", style="font-weight: bold;"),
    tags.p(
        """
        This is a 
        """,
        tags.a("public interactive dashboard", href=("https://anjie-liu.shinyapps.io/Real_Estate/"), target="_blank"),
        """
         exploring the real estate data from Houston and Austin large areas dating from 1990 to 2021.
        """,
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

real_dataset_information = TagList(
    tags.h5("Data Description", style="font-weight: bold;"),
    tags.p(
        """
        The dataset is scraped from 
        """,
        tags.a("Texas Real Estate Research Center at Texas A&M University", href="https://www.recenter.tamu.edu", target="_blank"),
        style="""
        text-align: left;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.hr(),

    tags.h5("Data Size", style="font-weight: bold;"),
    tags.ul(
        tags.li(
            tags.p("""32 years * 2 regions * 10 variables"""),
        ),
    ),
)
def info_modal():
    modal_show(
        modal(
            tags.strong(tags.h3("Greetings!")),
            tags.p(),
            tags.p(
                """
            You are about to explore a collection of Anjie's projects and learn more about her!\n
            """,
                style="""
                text-align: justify;
                word-break:break-word;
                hyphens: auto;
                """,
            ),
            tags.p(
                """
            Hope you enjoy!
            """,
                style="""
                text-align: justify;
                word-break:break-word;
                hyphens: auto;
                """,
            ),
            size="l",
            easy_close=True,
            footer=modal_button("Great!", style="material-circle"),
        )
    )
