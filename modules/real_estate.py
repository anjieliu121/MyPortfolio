from utils.description import (
    real_about_text,
    real_dataset_information,
)
from shiny import App, Inputs, Outputs, Session, render, ui
from shiny import ui, module, reactive


########################################################################################################################
# UI
########################################################################################################################
@module.ui
def real_ui():
    return ui.tags.div(
        # left pane
        ui.tags.div(
            ui.tags.div(
                # About
                real_about_text,
                ui.tags.hr(),
                # Dataset Information
                real_dataset_information,

                # style
                style="margin: 10px;",

            ),
            style="flex: 1; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin: 10px;",
        ),
        # right pane
        ui.tags.div(
            ui.br(),
            ui.br(),
            ui.output_ui('rshiny'),
            style="flex: 3; margin: 30px;",
        ),
        style="display: flex;",
    )




########################################################################################################################
# Server
########################################################################################################################
@module.server
def real_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.ui
    def rshiny():
        return ui.tags.iframe(
            height="800",
            width="1000",
            frameborder="no",
            src="https://anjie-liu.shinyapps.io/Real_Estate/",
        )


