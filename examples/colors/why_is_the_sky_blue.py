"""
Why is the sky blue? - A demonstration using Bokeh sky colors

This example demonstrates the physics behind why the sky appears blue using
Bokeh's sky-related color palette. It provides educational content about
Rayleigh scattering and showcases the available sky colors.

The sky appears blue due to Rayleigh scattering, where shorter wavelengths
(blue light ~450-495 nm) are scattered more strongly than longer wavelengths
by molecules in Earth's atmosphere. The scattering intensity is proportional
to 1/λ⁴, where λ is the wavelength.

This example can be run when Bokeh dependencies (including numpy) are available.
"""

# Import sky-related colors from Bokeh
from bokeh.colors.named import skyblue, lightskyblue, deepskyblue

def explain_sky_colors():
    """
    Explain why the sky is blue and demonstrate Bokeh's sky colors.
    """
    print("Why is the sky blue?")
    print("=" * 50)
    print()
    print("The sky appears blue due to a phenomenon called Rayleigh scattering.")
    print("When sunlight enters Earth's atmosphere, it collides with tiny gas molecules.")
    print("Blue light has a shorter wavelength (~450-495 nm) compared to red light (~620-750 nm).")
    print()
    print("According to Rayleigh scattering theory, the scattering intensity is")
    print("proportional to 1/λ⁴, where λ is the wavelength of light.")
    print("This means blue light is scattered about 5 times more than red light!")
    print()
    print("Available sky colors in Bokeh:")
    print("-" * 30)
    print(f"skyblue:      RGB({skyblue.r}, {skyblue.g}, {skyblue.b})      - #{skyblue.r:02x}{skyblue.g:02x}{skyblue.b:02x}")
    print(f"lightskyblue: RGB({lightskyblue.r}, {lightskyblue.g}, {lightskyblue.b})     - #{lightskyblue.r:02x}{lightskyblue.g:02x}{lightskyblue.b:02x}")
    print(f"deepskyblue:  RGB({deepskyblue.r}, {deepskyblue.g}, {deepskyblue.b})       - #{deepskyblue.r:02x}{deepskyblue.g:02x}{deepskyblue.b:02x}")
    print()
    print("These colors can be used in Bokeh visualizations to represent:")
    print("- Sky backgrounds in weather visualizations")
    print("- Ocean and water themes")
    print("- Scientific diagrams about light scattering")
    print("- Any visualization requiring natural blue tones")

if __name__ == "__main__":
    explain_sky_colors()
    
    # If numpy and full Bokeh are available, create interactive visualization
    try:
        import numpy as np
        from bokeh.plotting import figure, show
        from bokeh.models import HoverTool, Span
        from bokeh.layouts import column
        from bokeh.models.annotations import Title
        
        print("\nCreating interactive visualization...")
        
        # Create wavelength data (in nanometers) - visible light spectrum
        wavelengths = np.linspace(380, 700, 100)
        
        # Rayleigh scattering intensity (proportional to 1/λ⁴)
        scattering_intensity = 1 / (wavelengths ** 4)
        scattering_intensity = scattering_intensity / np.max(scattering_intensity)
        
        # Create the main plot
        p = figure(
            title="Rayleigh Scattering: Why the Sky is Blue",
            x_axis_label="Wavelength (nm)",
            y_axis_label="Relative Scattering Intensity",
            width=800,
            height=400
        )
        
        # Plot the scattering curve
        p.line(wavelengths, scattering_intensity, line_width=3, color=deepskyblue,
               legend_label="Scattering Intensity ∝ 1/λ⁴")
        
        # Add vertical lines for blue wavelength range
        blue_start = Span(location=450, dimension='height', line_color='blue', 
                          line_dash='dashed', line_width=2)
        blue_end = Span(location=495, dimension='height', line_color='blue', 
                        line_dash='dashed', line_width=2)
        p.add_layout(blue_start)
        p.add_layout(blue_end)
        
        show(p)
        
    except ImportError as e:
        print(f"\nInteractive visualization requires additional dependencies: {e}")
        print("The color demonstration above shows the core concept!")