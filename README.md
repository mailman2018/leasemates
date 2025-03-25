# LeaseMates Mobile App

LeaseMates is a mobile application designed to help roommates manage their shared living space efficiently. The app provides features for maintenance requests, communication, and general apartment management.

## Features

- 🔐 **Authentication**: Secure login and registration system
- 🏠 **Dashboard**: Overview of maintenance requests, messages, and upcoming events
- 🔧 **Maintenance**: Create and track maintenance requests with priority levels
- 💬 **Messaging**: Real-time communication between roommates
- 👤 **Profile Management**: User settings and preferences
- 🔔 **Notifications**: Stay updated with important events and messages

## Prerequisites

Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/) (v6 or higher)
- [Expo CLI](https://docs.expo.dev/get-started/installation/)
- [Expo Go](https://expo.dev/client) app on your mobile device (for testing)
- iOS Simulator (for Mac users) or Android Studio (for Android emulation)

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mailman2018/leasemates.git
   cd leasemates/leasemates-mobile
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Environment Setup**
   Create a `.env` file in the root directory with the following variables:
   ```
   API_URL=http://localhost:8000/api
   ```

4. **Start the Development Server**
   ```bash
   npx expo start
   ```

## Testing the App

### Using Expo Go (Recommended for Quick Testing)

1. Install the Expo Go app on your mobile device:
   - [iOS App Store](https://apps.apple.com/app/expo-go/id982107779)
   - [Android Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)

2. Start the development server:
   ```bash
   npx expo start
   ```

3. Scan the QR code:
   - iOS: Use your phone's camera
   - Android: Use the Expo Go app's QR scanner

### Using Simulators/Emulators

#### iOS Simulator (Mac only)
1. Install Xcode from the Mac App Store
2. Install iOS Simulator through Xcode
3. Run:
   ```bash
   npx expo start --ios
   ```

#### Android Emulator
1. Install Android Studio
2. Set up an Android Virtual Device (AVD)
3. Run:
   ```bash
   npx expo start --android
   ```

## Testing Features

1. **Authentication**
   - Register a new account
   - Login with existing credentials
   - Test password validation
   - Verify error handling

2. **Maintenance Requests**
   - Create a new maintenance request
   - Set different priority levels
   - View request status
   - Test request updates

3. **Messaging**
   - Send messages to other users
   - View message history
   - Test real-time updates

4. **Profile Management**
   - Update profile information
   - Change settings
   - Test logout functionality

## Development Notes

- The app uses React Native with Expo for cross-platform development
- State management is handled through React Context
- API calls are managed through Axios with interceptors
- UI components are built with React Native Paper

## Troubleshooting

Common issues and solutions:

1. **Metro Bundler Issues**
   ```bash
   npx expo start --clear
   ```

2. **Dependency Issues**
   ```bash
   rm -rf node_modules
   npm install
   ```

3. **Expo Go Connection Issues**
   - Ensure your phone and computer are on the same network
   - Try using a tunnel connection:
     ```bash
     npx expo start --tunnel
     ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the development team.
