from utils.description import (
    co2_about_text,
    co2_dataset_information,
)
from shiny import App, Inputs, Outputs, Session, render, ui
from shiny import ui, module, reactive


########################################################################################################################
# UI
########################################################################################################################
@module.ui
def co2_ui():
    return ui.tags.div(
        # left pane
        ui.tags.div(
            ui.tags.div(
                # About
                co2_about_text,
                ui.tags.hr(),
                # Dataset Information
                co2_dataset_information,

                # style
                style="margin: 10px;",

            ),
            style="flex: 1; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin: 10px;",
        ),
        # right pane
        ui.tags.div(
            ui.br(),
            ui.br(),
            ui.output_ui('web'),
            style="flex: 3; margin: 30px;",
        ),
        style="display: flex;",
    )




########################################################################################################################
# Server
########################################################################################################################
@module.server
def co2_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.ui
    def web():
        return ui.tags.iframe(
            height="800",
            width="1000",
            frameborder="no",
            src="https://anjie-liu.shinyapps.io/sustainability-world-map/",
        )