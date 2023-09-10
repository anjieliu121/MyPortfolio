from typing import List

from shiny import App, Inputs, Outputs, Session, reactive, ui
from shiny.types import NavSetArg

from utils.description import info_modal
from modules import cosmology, sustainability, housing, well_production



def nav_controls(prefix: str) -> List[NavSetArg]:
    return [

        ui.nav("Cosmology", cosmology.cosmo_ui(id="cosmo")),
        ui.nav("Sustainability", sustainability.co2_ui(id="co2")),
        ui.nav("Well Production", well_production.well_ui(id="well")),
        ui.nav("Housing", housing.house_ui(id="house")),
        #ui.nav("Hospital Care", tab_e_content()),
        #ui.nav("WHO AM I?", tab_f_content()),

        ui.nav_spacer(),

        ui.nav_control(
            ui.a(
                "GitHub",
                href="https://github.com/anjieliu121",
                target="_blank",
            )
        ),
        ui.nav_control(
            ui.a(
                "LinkedIn",
                href="https://www.linkedin.com/in/anjie-liu-a73574253/",
                target="_blank",
            )
        ),

    ]


app_ui = ui.div(
    ui.page_navbar(
        *nav_controls("page_navbar"),
        title="Anjie Liu",
        bg="#845BB3",
        inverse=True,
        id="navbar_id",
        footer=ui.div(
            {"style": "width:80%;margin: 0 auto;"},
            ui.tags.style(
                """
                h4 {
                    margin-top: 3em;
                }
                """
            ),
        ),
        position = "fixed-top",

    ),

)



def server(input: Inputs, output: Outputs, session: Session):
    info_modal()

    @reactive.Effect
    @reactive.event(input.info_icon)
    def _():
        info_modal()

    cosmology.cosmo_server("cosmo")
    sustainability.co2_server("co2")
    housing.house_server("house")
    well_production.well_server("well")

app = App(app_ui, server)
