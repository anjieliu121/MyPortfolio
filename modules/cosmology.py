from utils.description import (
    cosmo_about_text,
    cosmo_dataset_information,
)
from shiny import App, Inputs, Outputs, Session, render, ui
from shiny import ui, module, reactive
from shiny.types import ImgData
from pathlib import Path


########################################################################################################################
# UI
########################################################################################################################
@module.ui
def cosmo_ui():
    return ui.tags.div(
        # left pane
        ui.tags.div(
            ui.tags.div(
                # About
                cosmo_about_text,
                ui.tags.hr(),
                # Choose a profile
                ui.input_select(
                    id="profile",
                    label="Choose a Profile:",
                    choices={
                        "Gas Profile": {"t": "Temperature", "pnth": "Non-thermal Pressure", "pth": "Thermal Pressure",
                                        "ptot": "Total Pressure", "rho_gas": "Gas Density", "e": "Entropy"},
                        "Dark Matter Profile": {"rho_dm": "Dark Matter Density"},
                    },
                ),
                ui.tags.hr(),
                # Dataset information
                cosmo_dataset_information,
                style="margin: 10px;",
            ),
            style="flex: 1; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin: 10px;",  # Add margin style
        ),
        # right pane
        ui.tags.div(

            ui.tags.div(

                ui.output_image("profile_img"),
                ui.output_image("shap_img"),
                style="display: flex; justify-content: space-between; margin: 100px;",
            ),

            ui.tags.div(
                ui.hr(),
                ui.h5(
                    """
                    Presentation Slides at the Baryon Paster Collaboration Meeting
                    """,
                    style="font-weight: bold; center;"),
                ui.output_ui("pres_pdf"),
                style="margin: 40px;",
            ),
        ),


        style="display: flex;",
    )


########################################################################################################################
# Server
########################################################################################################################
@module.server
def cosmo_server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.image
    def profile_img():
        choice = input.profile()

        dir = Path(__file__).resolve().parent.parent
        img: ImgData = {"src": str(dir/"www/cosmology/profiles"/(choice+".png")), "width": "450px", "height":"450px"}
        return img

    @output
    @render.image
    def shap_img():
        choice = input.profile()
        dir = Path(__file__).resolve().parent.parent
        img: ImgData = {"src": str(dir/"www/cosmology/shap"/(choice+".png")), "width": "450px", "height":"450px"}
        return img

    @output
    @render.ui
    def pres_pdf():
        return ui.tags.iframe(
            height="500",
            width="1000",
            frameborder="no",
            src="https://drive.google.com/file/d/1udohd8mw7ycA3td2ES1pQ1vhezQ4gnCb/preview",
        )