# Halal Feasto - Digital Menu

A modern, responsive digital menu website for Halal Feasto restaurant featuring interactive navigation, multimedia content, and comprehensive menu sections.

## Features

- 🍔 **Interactive Menu Categories** - Burgers, Sandwiches, Gyros, Platters, and more
- 📱 **Responsive Design** - Optimized for all device sizes
- 🎬 **Video Integration** - Dynamic video backgrounds showcasing food preparation
- 🏪 **Store Imagery** - High-quality photos of food items and store
- 🎯 **Smooth Navigation** - Active section highlighting and smooth scrolling
- 🥗 **Detailed Descriptions** - Ingredient-based menu descriptions
- 💳 **Pricing Information** - Clear pricing with combo options

## Menu Sections

- **Burgers** - Cheeseburger, Jumbo Burger, Asylum Burger, Toxic Burger, Garden Delight
- **Sandwiches** - Krunchy Chicken, Grilled Chicken, Fish Sandwiches
- **Gyros** - Chicken, Lamb, Kofta, Fish, Falafel varieties
- **Platters** - Complete meals with rice, salad, and sides
- **Sides** - Fries, Mozzarella Sticks, Loaded Fries
- **Desserts** - Baklava, Brownies, Cakes
- **Beverages** - Soft drinks, Fresh juices

## Technologies Used

- **HTML5** - Semantic markup and modern web standards
- **CSS3** - Custom styling with Tailwind CSS framework
- **JavaScript** - Interactive navigation and scroll spy functionality
- **Video HTML5** - Embedded cooking demonstration videos
- **Responsive Images** - Optimized food photography

## File Structure

```
Resturant-Pamplet-Project/
├── menu.html              # Main menu page
├── ingredients.csv         # Menu ingredient data
├── images/                 # Food and restaurant images
│   ├── Burger/            # Burger images
│   ├── Sandwiches/        # Sandwich images
│   ├── Gyros/             # Gyro images
│   ├── Store/             # Restaurant photos
│   └── logo/              # Brand logos
├── video/                 # Cooking demonstration videos
│   └── making.mp4         # Food preparation video
├── README.md              # Project documentation
└── .gitignore            # Git ignore rules
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd Resturant-Pamplet-Project
   ```

2. Open `menu.html` in your web browser or serve using a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   ```

3. Navigate to `http://localhost:8000` in your browser

## Customization

### Adding New Menu Items
1. Add item images to the appropriate folder in `/images/`
2. Update the HTML structure in `menu.html`
3. Add ingredient information to `ingredients.csv`

### Modifying Styles
- The project uses Tailwind CSS classes for styling
- Custom CSS can be added in the `<style>` section of `menu.html`

### Updating Videos
- Replace `making.mp4` in the `/video/` folder
- Ensure video format is MP4 for maximum compatibility

## Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Considerations

- Images are optimized for web display
- Videos use autoplay with mute for better user experience
- Responsive design reduces load on mobile devices
- Lazy loading implemented where applicable

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support regarding this digital menu:
- Restaurant: Halal Feasto
- Website: [Your website URL]
- Email: [Your contact email]

---

**Note**: This is a static website project designed for restaurant menu display. For dynamic features like online ordering, additional backend development would be required.