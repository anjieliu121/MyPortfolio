from utils.description import (
    me_about_text,
)
from shiny import Inputs, Outputs, Session, render, ui, module
from shiny.types import ImgData
from pathlib import Path


########################################################################################################################
# UI
########################################################################################################################
@module.ui
def me_ui():
    return ui.tags.div(
        # left pane
        ui.tags.div(
            style="flex: 1; margin: 200;",
        ),
        # middle pane
        ui.tags.div(
            ui.tags.div(
                # About
                me_about_text,
                ui.output_image("smiley_img"),
                ui.tags.hr(),
                style="margin: 30px;",
            ),
            style="flex: 2; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);",  # Add margin style
        ),
        # right pane
        ui.tags.div(
            style="flex: 1;",
        ),
        style="display: flex;",
    )




########################################################################################################################
# Server
########################################################################################################################
@module.server
def me_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.image
    def smiley_img():
        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": "/Users/anjieliu/Documents/MyHackathons/MyPortfolio/www/smiley.png", "width": "350", "height": "350"}
        return img

