from utils.description import (
    well_about_text,
    well_dataset_information,
)
from shiny import App, Inputs, Outputs, Session, render, ui
from shiny import ui, module, reactive


########################################################################################################################
# UI
########################################################################################################################
@module.ui
def well_ui():
    return ui.tags.div(
        # left pane
        ui.tags.div(
            ui.tags.div(
                # About
                well_about_text,
                ui.tags.hr(),
                # Dataset Information
                well_dataset_information,

                # style
                style="margin: 10px;",

            ),
            style="flex: 1; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin: 10px;",
        ),
        # right pane
        ui.tags.div(
            ui.br(),
            ui.br(),
            ui.output_ui('pdf'),
            style="flex: 3; margin: 30px;",
        ),
        style="display: flex;",
    )




########################################################################################################################
# Server
########################################################################################################################
@module.server
def well_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.ui
    def pdf():
        return ui.tags.iframe(
            height="800",
            width="1000",
            frameborder="no",
            src="/Users/anjieliu/Documents/MyHackathons/MyPortfolio/www/DRAFT_well_production.pdf",
        )