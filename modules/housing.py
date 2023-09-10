from utils.description import (
    house_about_text,
    house_dataset_information,
)
from shiny import Inputs, Outputs, Session, render, ui, module
from shiny.types import ImgData
from pathlib import Path


########################################################################################################################
# UI
########################################################################################################################
@module.ui
def house_ui():
    return ui.tags.div(
        # left pane
        ui.tags.div(
            ui.tags.div(
                # About
                house_about_text,
                ui.tags.hr(),
                # Dataset Information
                house_dataset_information,
                style="margin: 10px;",
            ),
            style="flex: 1; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin: 10px;",  # Add margin style
        ),
        ui.tags.div(
            ui.br(),
            ui.br(),
            ui.output_image('house_img1'),
            ui.br(),
            ui.br(),
            ui.br(),
            ui.br(),
            ui.br(),
            ui.br(),
            ui.br(),
            ui.output_image('house_img2'),
            style="flex: 3; margin: 30px;",
        ),
        style="display: flex;",
    )




########################################################################################################################
# Server
########################################################################################################################
@module.server
def house_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.image
    def house_img1():
        dir = Path(__file__).resolve().parent.parent
        img: ImgData = {"src": str(dir / "www/housing/option1.png"), "width": "1000px", "height": "650px"}
        return img

    @output
    @render.image
    def house_img2():
        dir = Path(__file__).resolve().parent.parent
        img: ImgData = {"src": str(dir / "www/housing/option2.png"), "width": "1000px", "height": "650px"}
        return img


    # the app link is not working
    @output
    @render.ui
    def dash():
        return ui.tags.iframe(
            height="800",
            width="100%",
            frameborder="no",
            src="https://racial-disparity-index-tool.streamlit.app",
        )

